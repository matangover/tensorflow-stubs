# Stubs for tensorflow.contrib.opt.python.training.multitask_optimizer_wrapper (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, clip_ops as clip_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer
from typing import Any as Any

class MultitaskOptimizerWrapper:
    def __init__(self, opt: Any) -> None: ...
    def __getattr__(self, name: Any): ...

def clip_gradients_by_global_norm(gradients_variables: Any, clip_norm: float = ...): ...