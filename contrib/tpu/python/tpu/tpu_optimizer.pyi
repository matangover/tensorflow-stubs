# Stubs for tensorflow.contrib.tpu.python.tpu.tpu_optimizer (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.tpu.python.ops import tpu_ops as tpu_ops
from tensorflow.contrib.tpu.python.tpu import tpu_function as tpu_function
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops.losses import losses as losses
from tensorflow.python.training import optimizer as optimizer
from typing import Any as Any, Optional as Optional

class CrossShardOptimizer(optimizer.Optimizer):
    def __init__(self, opt: Any, reduction: Any = ..., name: str = ..., group_assignment: Optional[Any] = ...) -> None: ...
    def compute_gradients(self, loss: Any, var_list: Optional[Any] = ..., **kwargs: Any): ...
    def apply_gradients(self, grads_and_vars: Any, global_step: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def get_slot(self, *args: Any, **kwargs: Any): ...
    def get_slot_names(self, *args: Any, **kwargs: Any): ...
    def variables(self): ...
