# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Provides Qt3DExtras classes and functions."""

# Local imports
from . import PYQT5, PYSIDE2, PythonQtError, PYSIDE_VERSION
from .py3compat import PY2

if PYQT5:
    from PyQt5.Qt3DExtras import *
elif PYSIDE2:
    if not PY2 or (PY2 and PYSIDE_VERSION < "5.12.4"):
        # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
        import PySide2.Qt3DExtras as __temp
        import inspect

        for __name in inspect.getmembers(__temp.Qt3DExtras):
            globals()[__name[0]] = __name[1]
    else:
        raise PythonQtError("A bug in Shiboken prevents this")
else:
    raise PythonQtError("No Qt bindings could be found")
