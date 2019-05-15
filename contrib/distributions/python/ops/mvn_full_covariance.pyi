# Stubs for tensorflow.contrib.distributions.python.ops.mvn_full_covariance (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.distributions.python.ops import mvn_tril as mvn_tril
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, linalg_ops as linalg_ops
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class MultivariateNormalFullCovariance(mvn_tril.MultivariateNormalTriL):
    def __init__(self, loc: Optional[Any] = ..., covariance_matrix: Optional[Any] = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
