# Stubs for tensorflow.contrib.distributions.python.ops.logistic (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, nn_ops as nn_ops, random_ops as random_ops
from tensorflow.python.ops.distributions import distribution as distribution
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any

class Logistic(distribution.Distribution):
    def __init__(self, loc: Any, scale: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...
