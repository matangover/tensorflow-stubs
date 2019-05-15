# Stubs for tensorflow.contrib.specs.python.specs_lib (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any

QUOTED: Any
KEYWORDS: Any
debug_: bool

def check_keywords(spec: Any) -> None: ...
def get_positional(args: Any, kw: Any, kw_overrides: bool = ...): ...

class Composable:
    def __or__(self, f: Any): ...
    def __add__(self, g: Any): ...
    def __mul__(self, g: Any): ...
    def __pow__(self, n: Any): ...

class Callable(Composable):
    f: Any = ...
    def __init__(self, f: Any) -> None: ...
    def funcall(self, x: Any): ...

class Operator(Composable):
    op: Any = ...
    funs: Any = ...
    def __init__(self, op: Any, *args: Any) -> None: ...
    def funcall(self, x: Any): ...

class Function(Composable):
    f: Any = ...
    args: Any = ...
    kw: Any = ...
    def __init__(self, f: Any, *args: Any, **kw: Any) -> None: ...
    def __call__(self, *args: Any, **kw: Any): ...
    def funcall(self, x: Any): ...

class Composition(Composable):
    f: Any = ...
    g: Any = ...
    def __init__(self, f: Any, g: Any) -> None: ...
    def funcall(self, x: Any): ...

def External(module_name: Any, function_name: Any): ...
def Import(statements: Any): ...
def debug(mode: bool = ...) -> None: ...