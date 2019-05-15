# Stubs for tensorflow.contrib.distributions.python.ops.vector_laplace_linear_operator (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.distributions.python.ops import bijectors as bijectors, distribution_util as distribution_util
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.distributions import laplace as laplace, transformed_distribution as transformed_distribution
from tensorflow.python.ops.linalg import linalg as linalg
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class VectorLaplaceLinearOperator(transformed_distribution.TransformedDistribution):
    def __init__(self, loc: Optional[Any] = ..., scale: Optional[Any] = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...
