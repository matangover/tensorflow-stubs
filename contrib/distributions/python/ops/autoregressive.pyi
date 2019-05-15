# Stubs for tensorflow.contrib.distributions.python.ops.autoregressive (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops.distributions import distribution as distribution_lib
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class Autoregressive(distribution_lib.Distribution):
    def __init__(self, distribution_fn: Any, sample0: Optional[Any] = ..., num_steps: Optional[Any] = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def distribution_fn(self): ...
    @property
    def sample0(self): ...
    @property
    def num_steps(self): ...
    @property
    def distribution0(self): ...
