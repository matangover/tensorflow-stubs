# Stubs for tensorflow.contrib.framework.python.ops.sort_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn_ops as nn_ops
from typing import Any as Any, Optional as Optional

def sort(values: Any, axis: int = ..., direction: str = ..., name: Optional[Any] = ...): ...
def argsort(values: Any, axis: int = ..., direction: str = ..., stable: bool = ..., name: Optional[Any] = ...): ...
