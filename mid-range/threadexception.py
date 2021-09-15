import threading
import traceback
import warnings
from types import TracebackType
from typing import Any
from typing import Callable
from typing import Generator
from typing import Optional
from typing import Type

import pytest


# Copied from cpython/Lib/test/support/threading_helper.py, with modifications.
class catch_threading_exception:
    """Context manager catching threading.Thread exception using
    threading.excepthook.

    Storing exc_value using a custom hook can create a reference cycle. The
    reference cycle is broken explicitly when the context manager exits.

    Storing thread using a custom hook can resurrect it if it is set to an
    object which is being finalized. Exiting the context manager clears the
    stored object.

    Usage:
        with threading_helper.catch_threading_exception() as cm:
            # code spawning a thread which raises an exception
            ...
            # check the thread exception: use cm.args
            ...
        # cm.args attribute no longer exists at this point
        # (to break a reference cycle)
    """

    def __init__(self) -> None:
        # See https://github.com/python/typeshed/issues/4767 regarding the underscore.
        self.args: Optional["threading._ExceptHookArgs"] = None
        self._old_hook: Optional[Callable[["threading._ExceptHookArgs"], Any]] = None

    def _hook(self, args: "threading._ExceptHookArgs") -> None:
        self.args = args

    def __enter__(self) -> "catch_threading_exception":
        self._old_hook = threading.excepthook
        threading.excepthook = self._hook
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        assert self._old_hook is not None
        threading.excepthook = self._old_hook
        self._old_hook = None
        del self.args


def thread_exception_runtest_hook() -> Generator[None, None, None]:
    with catch_threading_exception() as cm:
        yield
        if cm.args:
            if cm.args.thread is not None:
                thread_name = cm.args.thread.name
            else:
                thread_name = "<unknown>"
            msg = f"Exception in thread {thread_name}\n\n"
            msg += "".join(
                traceback.format_exception(
                    cm.args.exc_type, cm.args.exc_value, cm.args.exc_traceback
                )
            )
            warnings.warn(pytest.PytestUnhandledThreadExceptionWarning(msg))


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_setup() -> Generator[None, None, None]:
    yield from thread_exception_runtest_hook()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_call() -> Generator[None, None, None]:
    yield from thread_exception_runtest_hook()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_teardown() -> Generator[None, None, None]:
    yield from thread_exception_runtest_hook()
