# Stubs for tensorflow.contrib.optimizer_v2.gradient_descent (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from tensorflow.python.training import training_ops as training_ops
from typing import Any as Any

class GradientDescentOptimizer(optimizer_v2.OptimizerV2):
    def __init__(self, learning_rate: Any, use_locking: bool = ..., name: str = ...) -> None: ...
