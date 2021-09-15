from abc import abstractproperty

from parso.tree import search_ancestor

from jedi import debug
from jedi import settings
from jedi.inference import compiled
from jedi.inference.compiled.value import CompiledValueFilter
from jedi.inference.helpers import values_from_qualified_names, is_big_annoying_library
from jedi.inference.filters import AbstractFilter, AnonymousFunctionExecutionFilter
from jedi.inference.names import ValueName, TreeNameDefinition, ParamName, NameWrapper
from jedi.inference.base_value import (
    Value,
    NO_VALUES,
    ValueSet,
    iterator_to_value_set,
    ValueWrapper,
)
from jedi.inference.lazy_value import LazyKnownValue, LazyKnownValues
from jedi.inference.cache import inference_state_method_cache
from jedi.inference.arguments import ValuesArguments, TreeArgumentsWrapper
from jedi.inference.value.function import (
    FunctionValue,
    FunctionMixin,
    OverloadedFunctionValue,
    BaseFunctionExecutionContext,
    FunctionExecutionContext,
    FunctionNameInClass,
)
from jedi.inference.value.klass import ClassFilter
from jedi.inference.value.dynamic_arrays import get_dynamic_array_instance
from jedi.parser_utils import function_is_staticmethod, function_is_classmethod


class InstanceExecutedParamName(ParamName):
    def __init__(self, instance, function_value, tree_name):
        super().__init__(function_value, tree_name, arguments=None)
        self._instance = instance

    def infer(self):
        return ValueSet([self._instance])

    def matches_signature(self):
        return True


class AnonymousMethodExecutionFilter(AnonymousFunctionExecutionFilter):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instance = instance

    def _convert_param(self, param, name):
        if param.position_index == 0:
            if function_is_classmethod(self._function_value.tree_node):
                return InstanceExecutedParamName(
                    self._instance.py__class__(), self._function_value, name
                )
            elif not function_is_staticmethod(self._function_value.tree_node):
                return InstanceExecutedParamName(
                    self._instance, self._function_value, name
                )
        return super()._convert_param(param, name)


class AnonymousMethodExecutionContext(BaseFunctionExecutionContext):
    def __init__(self, instance, value):
        super().__init__(value)
        self.instance = instance

    def get_filters(self, until_position=None, origin_scope=None):
        yield AnonymousMethodExecutionFilter(
            self.instance,
            self,
            self._value,
            until_position=until_position,
            origin_scope=origin_scope,
        )

    def get_param_names(self):
        param_names = list(self._value.get_param_names())
        # set the self name
        param_names[0] = InstanceExecutedParamName(
            self.instance, self._value, param_names[0].tree_name
        )
        return param_names


class MethodExecutionContext(FunctionExecutionContext):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = instance


class AbstractInstanceValue(Value):
    api_type = "instance"

    def __init__(self, inference_state, parent_context, class_value):
        super().__init__(inference_state, parent_context)
        # Generated instances are classes that are just generated by self
        # (No arguments) used.
        self.class_value = class_value

    def is_instance(self):
        return True

    def get_qualified_names(self):
        return self.class_value.get_qualified_names()

    def get_annotated_class_object(self):
        return self.class_value  # This is the default.

    def py__class__(self):
        return self.class_value

    def py__bool__(self):
        # Signalize that we don't know about the bool type.
        return None

    @abstractproperty
    def name(self):
        raise NotImplementedError

    def get_signatures(self):
        call_funcs = self.py__getattribute__("__call__").py__get__(
            self, self.class_value
        )
        return [s.bind(self) for s in call_funcs.get_signatures()]

    def get_function_slot_names(self, name):
        # Searches for Python functions in classes.
        return []

    def execute_function_slots(self, names, *inferred_args):
        return ValueSet.from_sets(
            name.infer().execute_with_values(*inferred_args) for name in names
        )

    def get_type_hint(self, add_class_info=True):
        return self.py__name__()

    def __repr__(self):
        return "<%s of %s>" % (self.__class__.__name__, self.class_value)


class CompiledInstance(AbstractInstanceValue):
    # This is not really a compiled class, it's just an instance from a
    # compiled class.
    def __init__(self, inference_state, parent_context, class_value, arguments):
        super().__init__(inference_state, parent_context, class_value)
        self._arguments = arguments

    def get_filters(self, origin_scope=None, include_self_names=True):
        class_value = self.get_annotated_class_object()
        class_filters = class_value.get_filters(
            origin_scope=origin_scope, is_instance=True
        )
        for f in class_filters:
            yield CompiledInstanceClassFilter(self, f)

    @property
    def name(self):
        return compiled.CompiledValueName(self, self.class_value.name.string_name)

    def is_stub(self):
        return False


class _BaseTreeInstance(AbstractInstanceValue):
    @property
    def array_type(self):
        name = self.class_value.py__name__()
        if (
            name in ["list", "set", "dict"]
            and self.parent_context.get_root_context().is_builtins_module()
        ):
            return name
        return None

    @property
    def name(self):
        return ValueName(self, self.class_value.name.tree_name)

    def get_filters(self, origin_scope=None, include_self_names=True):
        class_value = self.get_annotated_class_object()
        if include_self_names:
            for cls in class_value.py__mro__():
                if not cls.is_compiled():
                    # In this case we're excluding compiled objects that are
                    # not fake objects. It doesn't make sense for normal
                    # compiled objects to search for self variables.
                    yield SelfAttributeFilter(
                        self, class_value, cls.as_context(), origin_scope
                    )

        class_filters = class_value.get_filters(
            origin_scope=origin_scope, is_instance=True
        )
        for f in class_filters:
            if isinstance(f, ClassFilter):
                yield InstanceClassFilter(self, f)
            elif isinstance(f, CompiledValueFilter):
                yield CompiledInstanceClassFilter(self, f)
            else:
                # Propably from the metaclass.
                yield f

    @inference_state_method_cache()
    def create_instance_context(self, class_context, node):
        new = node
        while True:
            func_node = new
            new = search_ancestor(new, "funcdef", "classdef")
            if class_context.tree_node is new:
                func = FunctionValue.from_context(class_context, func_node)
                bound_method = BoundMethod(self, class_context, func)
                if func_node.name.value == "__init__":
                    context = bound_method.as_context(self._arguments)
                else:
                    context = bound_method.as_context()
                break
        return context.create_context(node)

    def py__getattribute__alternatives(self, string_name):
        """
        Since nothing was inferred, now check the __getattr__ and
        __getattribute__ methods. Stubs don't need to be checked, because
        they don't contain any logic.
        """
        if self.is_stub():
            return NO_VALUES

        name = compiled.create_simple_object(self.inference_state, string_name)

        # This is a little bit special. `__getattribute__` is in Python
        # executed before `__getattr__`. But: I know no use case, where
        # this could be practical and where Jedi would return wrong types.
        # If you ever find something, let me know!
        # We are inversing this, because a hand-crafted `__getattribute__`
        # could still call another hand-crafted `__getattr__`, but not the
        # other way around.
        if is_big_annoying_library(self.parent_context):
            return NO_VALUES
        names = self.get_function_slot_names(
            "__getattr__"
        ) or self.get_function_slot_names("__getattribute__")
        return self.execute_function_slots(names, name)

    def py__getitem__(self, index_value_set, contextualized_node):
        names = self.get_function_slot_names("__getitem__")
        if not names:
            return super().py__getitem__(index_value_set, contextualized_node)

        args = ValuesArguments([index_value_set])
        return ValueSet.from_sets(name.infer().execute(args) for name in names)

    def py__iter__(self, contextualized_node=None):
        iter_slot_names = self.get_function_slot_names("__iter__")
        if not iter_slot_names:
            return super().py__iter__(contextualized_node)

        def iterate():
            for generator in self.execute_function_slots(iter_slot_names):
                yield from generator.py__next__(contextualized_node)

        return iterate()

    def py__next__(self, contextualized_node=None):
        name = u"__next__"
        next_slot_names = self.get_function_slot_names(name)
        if next_slot_names:
            yield LazyKnownValues(self.execute_function_slots(next_slot_names))
        else:
            debug.warning("Instance has no __next__ function in %s.", self)

    def py__call__(self, arguments):
        names = self.get_function_slot_names("__call__")
        if not names:
            # Means the Instance is not callable.
            return super().py__call__(arguments)

        return ValueSet.from_sets(name.infer().execute(arguments) for name in names)

    def py__get__(self, instance, class_value):
        """
        obj may be None.
        """
        # Arguments in __get__ descriptors are obj, class.
        # `method` is the new parent of the array, don't know if that's good.
        for cls in self.class_value.py__mro__():
            result = cls.py__get__on_class(self, instance, class_value)
            if result is not NotImplemented:
                return result

        names = self.get_function_slot_names("__get__")
        if names:
            if instance is None:
                instance = compiled.builtin_from_name(self.inference_state, "None")
            return self.execute_function_slots(names, instance, class_value)
        else:
            return ValueSet([self])

    def get_function_slot_names(self, name):
        # Python classes don't look at the dictionary of the instance when
        # looking up `__call__`. This is something that has to do with Python's
        # internal slot system (note: not __slots__, but C slots).
        for filter in self.get_filters(include_self_names=False):
            names = filter.get(name)
            if names:
                return names
        return []


class TreeInstance(_BaseTreeInstance):
    def __init__(self, inference_state, parent_context, class_value, arguments):
        # I don't think that dynamic append lookups should happen here. That
        # sounds more like something that should go to py__iter__.
        if (
            class_value.py__name__() in ["list", "set"]
            and parent_context.get_root_context().is_builtins_module()
        ):
            # compare the module path with the builtin name.
            if settings.dynamic_array_additions:
                arguments = get_dynamic_array_instance(self, arguments)

        super().__init__(inference_state, parent_context, class_value)
        self._arguments = arguments
        self.tree_node = class_value.tree_node

    # This can recurse, if the initialization of the class includes a reference
    # to itself.
    @inference_state_method_cache(default=None)
    def _get_annotated_class_object(self):
        from jedi.inference.gradual.annotation import (
            py__annotations__,
            infer_type_vars_for_execution,
        )

        args = InstanceArguments(self, self._arguments)
        for signature in self.class_value.py__getattribute__(
            "__init__"
        ).get_signatures():
            # Just take the first result, it should always be one, because we
            # control the typeshed code.
            funcdef = signature.value.tree_node
            if (
                funcdef is None
                or funcdef.type != "funcdef"
                or not signature.matches_signature(args)
            ):
                # First check if the signature even matches, if not we don't
                # need to infer anything.
                continue
            bound_method = BoundMethod(
                self, self.class_value.as_context(), signature.value
            )
            all_annotations = py__annotations__(funcdef)
            type_var_dict = infer_type_vars_for_execution(
                bound_method, args, all_annotations
            )
            if type_var_dict:
                defined, = self.class_value.define_generics(
                    infer_type_vars_for_execution(
                        signature.value, args, all_annotations
                    )
                )
                debug.dbg("Inferred instance value as %s", defined, color="BLUE")
                return defined
        return None

    def get_annotated_class_object(self):
        return self._get_annotated_class_object() or self.class_value

    def get_key_values(self):
        values = NO_VALUES
        if self.array_type == "dict":
            for i, (key, instance) in enumerate(self._arguments.unpack()):
                if key is None and i == 0:
                    values |= ValueSet.from_sets(
                        v.get_key_values()
                        for v in instance.infer()
                        if v.array_type == "dict"
                    )
                if key:
                    values |= ValueSet(
                        [compiled.create_simple_object(self.inference_state, key)]
                    )

        return values

    def py__simple_getitem__(self, index):
        if self.array_type == "dict":
            # Logic for dict({'foo': bar}) and dict(foo=bar)
            # reversed, because:
            # >>> dict({'a': 1}, a=3)
            # {'a': 3}
            # TODO tuple initializations
            # >>> dict([('a', 4)])
            # {'a': 4}
            for key, lazy_context in reversed(list(self._arguments.unpack())):
                if key is None:
                    values = ValueSet.from_sets(
                        dct_value.py__simple_getitem__(index)
                        for dct_value in lazy_context.infer()
                        if dct_value.array_type == "dict"
                    )
                    if values:
                        return values
                else:
                    if key == index:
                        return lazy_context.infer()
        return super().py__simple_getitem__(index)

    def __repr__(self):
        return "<%s of %s(%s)>" % (
            self.__class__.__name__,
            self.class_value,
            self._arguments,
        )


class AnonymousInstance(_BaseTreeInstance):
    _arguments = None


class CompiledInstanceName(NameWrapper):
    @iterator_to_value_set
    def infer(self):
        for result_value in self._wrapped_name.infer():
            if result_value.api_type == "function":
                yield CompiledBoundMethod(result_value)
            else:
                yield result_value


class CompiledInstanceClassFilter(AbstractFilter):
    def __init__(self, instance, f):
        self._instance = instance
        self._class_filter = f

    def get(self, name):
        return self._convert(self._class_filter.get(name))

    def values(self):
        return self._convert(self._class_filter.values())

    def _convert(self, names):
        return [CompiledInstanceName(n) for n in names]


class BoundMethod(FunctionMixin, ValueWrapper):
    def __init__(self, instance, class_context, function):
        super().__init__(function)
        self.instance = instance
        self._class_context = class_context

    def is_bound_method(self):
        return True

    @property
    def name(self):
        return FunctionNameInClass(self._class_context, super().name)

    def py__class__(self):
        c, = values_from_qualified_names(self.inference_state, "types", "MethodType")
        return c

    def _get_arguments(self, arguments):
        assert arguments is not None
        return InstanceArguments(self.instance, arguments)

    def _as_context(self, arguments=None):
        if arguments is None:
            return AnonymousMethodExecutionContext(self.instance, self)

        arguments = self._get_arguments(arguments)
        return MethodExecutionContext(self.instance, self, arguments)

    def py__call__(self, arguments):
        if isinstance(self._wrapped_value, OverloadedFunctionValue):
            return self._wrapped_value.py__call__(self._get_arguments(arguments))

        function_execution = self.as_context(arguments)
        return function_execution.infer()

    def get_signature_functions(self):
        return [
            BoundMethod(self.instance, self._class_context, f)
            for f in self._wrapped_value.get_signature_functions()
        ]

    def get_signatures(self):
        return [sig.bind(self) for sig in super().get_signatures()]

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self._wrapped_value)


class CompiledBoundMethod(ValueWrapper):
    def is_bound_method(self):
        return True

    def get_signatures(self):
        return [sig.bind(self) for sig in self._wrapped_value.get_signatures()]


class SelfName(TreeNameDefinition):
    """
    This name calculates the parent_context lazily.
    """

    def __init__(self, instance, class_context, tree_name):
        self._instance = instance
        self.class_context = class_context
        self.tree_name = tree_name

    @property
    def parent_context(self):
        return self._instance.create_instance_context(
            self.class_context, self.tree_name
        )

    def get_defining_qualified_value(self):
        return self._instance

    def infer(self):
        stmt = search_ancestor(self.tree_name, "expr_stmt")
        if stmt is not None:
            if stmt.children[1].type == "annassign":
                from jedi.inference.gradual.annotation import infer_annotation

                values = infer_annotation(
                    self.parent_context, stmt.children[1].children[1]
                ).execute_annotation()
                if values:
                    return values
        return super().infer()


class LazyInstanceClassName(NameWrapper):
    def __init__(self, instance, class_member_name):
        super().__init__(class_member_name)
        self._instance = instance

    @iterator_to_value_set
    def infer(self):
        for result_value in self._wrapped_name.infer():
            yield from result_value.py__get__(
                self._instance, self._instance.py__class__()
            )

    def get_signatures(self):
        return self.infer().get_signatures()

    def get_defining_qualified_value(self):
        return self._instance


class InstanceClassFilter(AbstractFilter):
    """
    This filter is special in that it uses the class filter and wraps the
    resulting names in LazyInstanceClassName. The idea is that the class name
    filtering can be very flexible and always be reflected in instances.
    """

    def __init__(self, instance, class_filter):
        self._instance = instance
        self._class_filter = class_filter

    def get(self, name):
        return self._convert(self._class_filter.get(name))

    def values(self):
        return self._convert(self._class_filter.values())

    def _convert(self, names):
        return [LazyInstanceClassName(self._instance, n) for n in names]

    def __repr__(self):
        return "<%s for %s>" % (self.__class__.__name__, self._class_filter)


class SelfAttributeFilter(ClassFilter):
    """
    This class basically filters all the use cases where `self.*` was assigned.
    """

    def __init__(self, instance, instance_class, node_context, origin_scope):
        super().__init__(
            class_value=instance_class,
            node_context=node_context,
            origin_scope=origin_scope,
            is_instance=True,
        )
        self._instance = instance

    def _filter(self, names):
        start, end = self._parser_scope.start_pos, self._parser_scope.end_pos
        names = [n for n in names if start < n.start_pos < end]
        return self._filter_self_names(names)

    def _filter_self_names(self, names):
        for name in names:
            trailer = name.parent
            if (
                trailer.type == "trailer"
                and len(trailer.parent.children) == 2
                and trailer.children[0] == "."
            ):
                if name.is_definition() and self._access_possible(name):
                    # TODO filter non-self assignments instead of this bad
                    #      filter.
                    if self._is_in_right_scope(trailer.parent.children[0], name):
                        yield name

    def _is_in_right_scope(self, self_name, name):
        self_context = self._node_context.create_context(self_name)
        names = self_context.goto(self_name, position=self_name.start_pos)
        return any(
            n.api_type == "param"
            and n.tree_name.get_definition().position_index == 0
            and n.parent_context.tree_node is self._parser_scope
            for n in names
        )

    def _convert_names(self, names):
        return [SelfName(self._instance, self._node_context, name) for name in names]

    def _check_flows(self, names):
        return names


class InstanceArguments(TreeArgumentsWrapper):
    def __init__(self, instance, arguments):
        super().__init__(arguments)
        self.instance = instance

    def unpack(self, func=None):
        yield None, LazyKnownValue(self.instance)
        yield from self._wrapped_arguments.unpack(func)
