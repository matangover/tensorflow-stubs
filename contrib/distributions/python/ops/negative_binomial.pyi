# Stubs for tensorflow.contrib.distributions.python.ops.negative_binomial (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.ops.distributions import distribution as distribution
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class NegativeBinomial(distribution.Distribution):
    def __init__(self, total_count: Any, logits: Optional[Any] = ..., probs: Optional[Any] = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def total_count(self): ...
    @property
    def logits(self): ...
    @property
    def probs(self): ...
