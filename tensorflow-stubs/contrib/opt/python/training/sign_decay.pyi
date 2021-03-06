# Stubs for tensorflow.contrib.opt.python.training.sign_decay (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

def get_linear_decay_fn(decay_steps: Any): ...
def get_cosine_decay_fn(decay_steps: Any, num_periods: float = ..., zero_after: Optional[Any] = ...): ...
def get_restart_decay_fn(decay_steps: Any, num_periods: int = ..., zero_after: Optional[Any] = ...): ...
