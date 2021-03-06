# Stubs for tensorflow.contrib.distributions.python.ops.bijectors.softplus (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, nn_ops as nn_ops
from tensorflow.python.ops.distributions import bijector as bijector
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class Softplus(bijector.Bijector):
    def __init__(self, hinge_softness: Optional[Any] = ..., validate_args: bool = ..., name: str = ...) -> None: ...
    @property
    def hinge_softness(self): ...
