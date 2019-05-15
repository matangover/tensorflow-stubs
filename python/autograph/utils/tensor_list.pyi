# Stubs for tensorflow.python.autograph.utils.tensor_list (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import list_ops as list_ops, tensor_array_ops as tensor_array_ops
from typing import Any as Any

def dynamic_list_append(target: Any, element: Any): ...

class TensorList:
    dtype: Any = ...
    shape: Any = ...
    def __init__(self, shape: Any, dtype: Any) -> None: ...
    list_: Any = ...
    def append(self, value: Any) -> None: ...
    def pop(self): ...
    def clear(self) -> None: ...
    def count(self): ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
