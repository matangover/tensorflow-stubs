# Stubs for tensorflow.python.ops.distributions.student_t (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, nn as nn, random_ops as random_ops, special_math_ops as special_math_ops
from tensorflow.python.ops.distributions import distribution as distribution
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

class StudentT(distribution.Distribution):
    def __init__(self, df: Any, loc: Any, scale: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def df(self): ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...

class StudentTWithAbsDfSoftplusScale(StudentT):
    def __init__(self, df: Any, loc: Any, scale: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
