# Stubs for tensorflow.contrib.recurrent.python.ops.recurrent (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, function as function, ops as ops
from tensorflow.python.ops import array_ops as array_ops, functional_ops as functional_ops, gradients_impl as gradients_impl, inplace_ops as inplace_ops, math_ops as math_ops
from tensorflow.python.ops.inplace_ops import alias_inplace_update as alias_inplace_update
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

class _Recurrent:
    def __init__(self, cell_fn: Any, cell_grad: Any, theta: Any, state0: Any, inputs: Any, max_input_length: Any, extras: Any, use_tpu: Any, aligned_end: bool = ...) -> None: ...
    def Compute(self): ...

def Recurrent(theta: Any, state0: Any, inputs: Any, cell_fn: Any, cell_grad: Optional[Any] = ..., extras: Optional[Any] = ..., max_input_length: Optional[Any] = ..., use_tpu: bool = ..., aligned_end: bool = ...): ...