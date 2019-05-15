# Stubs for tensorflow.python.ops.distributions.gamma (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, nn as nn, random_ops as random_ops
from tensorflow.python.ops.distributions import distribution as distribution, kullback_leibler as kullback_leibler
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

class Gamma(distribution.Distribution):
    def __init__(self, concentration: Any, rate: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def concentration(self): ...
    @property
    def rate(self): ...

class GammaWithSoftplusConcentrationRate(Gamma):
    def __init__(self, concentration: Any, rate: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...