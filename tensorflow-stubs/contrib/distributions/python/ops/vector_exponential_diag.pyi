# Stubs for tensorflow.contrib.distributions.python.ops.vector_exponential_diag (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.distributions.python.ops import distribution_util as distribution_util, vector_exponential_linear_operator as vector_exponential_linop
from tensorflow.python.framework import ops as ops
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class VectorExponentialDiag(vector_exponential_linop.VectorExponentialLinearOperator):
    def __init__(self, loc: Optional[Any] = ..., scale_diag: Optional[Any] = ..., scale_identity_multiplier: Optional[Any] = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...