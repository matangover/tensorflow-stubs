# Stubs for tensorflow.contrib.optimizer_v2.momentum (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.training import training_ops as training_ops
from typing import Any as Any

class MomentumOptimizer(optimizer_v2.OptimizerV2):
    def __init__(self, learning_rate: Any, momentum: Any, use_locking: bool = ..., name: str = ..., use_nesterov: bool = ...) -> None: ...
