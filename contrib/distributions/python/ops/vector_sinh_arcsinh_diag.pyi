# Stubs for tensorflow.contrib.distributions.python.ops.vector_sinh_arcsinh_diag (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.distributions.python.ops import bijectors as bijectors, distribution_util as distribution_util
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.ops.distributions import normal as normal, transformed_distribution as transformed_distribution
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class VectorSinhArcsinhDiag(transformed_distribution.TransformedDistribution):
    def __init__(self, loc: Optional[Any] = ..., scale_diag: Optional[Any] = ..., scale_identity_multiplier: Optional[Any] = ..., skewness: Optional[Any] = ..., tailweight: Optional[Any] = ..., distribution: Optional[Any] = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...
    @property
    def tailweight(self): ...
    @property
    def skewness(self): ...