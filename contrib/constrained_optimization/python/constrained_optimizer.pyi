# Stubs for tensorflow.contrib.constrained_optimization.python.constrained_optimizer (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, standard_ops as standard_ops
from typing import Any as Any, Optional as Optional

class ConstrainedOptimizer(metaclass=abc.ABCMeta):
    def __init__(self, optimizer: Any) -> None: ...
    @property
    def optimizer(self): ...
    def minimize_constrained(self, minimization_problem: Any, global_step: Optional[Any] = ..., var_list: Optional[Any] = ..., gate_gradients: Any = ..., aggregation_method: Optional[Any] = ..., colocate_gradients_with_ops: bool = ..., name: Optional[Any] = ..., grad_loss: Optional[Any] = ...): ...
    def minimize_unconstrained(self, minimization_problem: Any, global_step: Optional[Any] = ..., var_list: Optional[Any] = ..., gate_gradients: Any = ..., aggregation_method: Optional[Any] = ..., colocate_gradients_with_ops: bool = ..., name: Optional[Any] = ..., grad_loss: Optional[Any] = ...): ...
    def minimize(self, minimization_problem: Any, unconstrained_steps: Optional[Any] = ..., global_step: Optional[Any] = ..., var_list: Optional[Any] = ..., gate_gradients: Any = ..., aggregation_method: Optional[Any] = ..., colocate_gradients_with_ops: bool = ..., name: Optional[Any] = ..., grad_loss: Optional[Any] = ...): ...
