# Stubs for tensorflow.contrib.distributions.python.ops.bijectors.gumbel (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.distributions import bijector as bijector
from tensorflow.python.util import deprecation as deprecation

class Gumbel(bijector.Bijector):
    def __init__(self, loc: float = ..., scale: float = ..., validate_args: bool = ..., name: str = ...) -> None: ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...