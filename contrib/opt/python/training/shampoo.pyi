# Stubs for tensorflow.contrib.opt.python.training.shampoo (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.opt.python.training import matrix_functions as matrix_functions
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, linalg_ops as linalg_ops, math_ops as math_ops, state_ops as state_ops
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.training import optimizer as optimizer
from typing import Any as Any

def GetParam(var: Any, timestep: Any): ...

class ShampooOptimizer(optimizer.Optimizer):
    def __init__(self, global_step: int = ..., max_matrix_size: int = ..., gbar_decay: float = ..., gbar_weight: float = ..., mat_gbar_decay: float = ..., mat_gbar_weight: float = ..., learning_rate: float = ..., svd_interval: int = ..., precond_update_interval: int = ..., epsilon: float = ..., alpha: float = ..., use_iterative_root: bool = ..., use_locking: bool = ..., name: str = ...) -> None: ...