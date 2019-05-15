# Stubs for tensorflow.contrib.compiler.jit (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.framework import ops as ops
from typing import Any as Any

class _XlaScope:
    count: Any = ...
    depth: Any = ...
    def __init__(self, count: Any, depth: Any) -> None: ...

def experimental_jit_scope(compile_ops: bool = ..., separate_compiled_gradients: bool = ...): ...
