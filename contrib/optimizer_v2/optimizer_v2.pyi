# Stubs for tensorflow.contrib.optimizer_v2.optimizer_v2 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, gradients as gradients, math_ops as math_ops, resource_variable_ops as resource_variable_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.training import distribution_strategy_context as distribution_strategy_context, optimizer as optimizer_v1, slot_creator as slot_creator
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

class _OptimizableVariable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def target(self) -> Any: ...
    @abc.abstractmethod
    def update_op(self, optimizer: Any, g: Any, *args: Any) -> Any: ...

class _RefVariableProcessor(_OptimizableVariable):
    def __init__(self, v: Any) -> None: ...
    def target(self): ...
    def update_op(self, optimizer: Any, g: Any, *args: Any): ...

class _DenseReadResourceVariableProcessor(_OptimizableVariable):
    def __init__(self, v: Any) -> None: ...
    def target(self): ...
    def update_op(self, optimizer: Any, g: Any, *args: Any): ...

class _DenseResourceVariableProcessor(_OptimizableVariable):
    def __init__(self, v: Any) -> None: ...
    def target(self): ...
    def update_op(self, optimizer: Any, g: Any, *args: Any): ...

class _TensorProcessor(_OptimizableVariable):
    def __init__(self, v: Any) -> None: ...
    def target(self): ...
    def update_op(self, optimizer: Any, g: Any, *args: Any) -> None: ...

class _OptimizerV2State:
    def __init__(self, op_name: Any) -> None: ...
    def create_slot(self, var: Any, val: Any, slot_name: Any, optional_op_name: Optional[Any] = ...): ...
    def create_slot_with_initializer(self, var: Any, initializer: Any, shape: Any, dtype: Any, slot_name: Any, optional_op_name: Optional[Any] = ...): ...
    def zeros_slot(self, var: Any, slot_name: Any, optional_op_name: Optional[Any] = ...): ...
    def get_slot(self, var: Any, name: Any): ...
    def get_slot_names(self): ...
    def create_non_slot(self, initial_value: Any, name: Any, colocate_with: Optional[Any] = ...): ...
    def get_non_slot(self, name: Any): ...
    def get_hyper(self, name: Any, dtype: Optional[Any] = ...): ...

class OptimizerV2(optimizer_v1.Optimizer):
    GATE_NONE: int = ...
    GATE_OP: int = ...
    GATE_GRAPH: int = ...
    def __init__(self, use_locking: Any, name: Any) -> None: ...
    def minimize(self, loss: Any, global_step: Optional[Any] = ..., var_list: Optional[Any] = ..., gate_gradients: Any = ..., aggregation_method: Optional[Any] = ..., colocate_gradients_with_ops: bool = ..., name: Optional[Any] = ..., grad_loss: Optional[Any] = ..., stop_gradients: Optional[Any] = ..., scale_loss_by_num_towers: Optional[Any] = ...): ...
    def compute_gradients(self, loss: Any, var_list: Optional[Any] = ..., gate_gradients: Any = ..., aggregation_method: Optional[Any] = ..., colocate_gradients_with_ops: bool = ..., grad_loss: Optional[Any] = ..., stop_gradients: Optional[Any] = ..., scale_loss_by_num_towers: Optional[Any] = ...): ...
    def apply_gradients(self, grads_and_vars: Any, global_step: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def get_slot(self, var: Any, name: Any): ...
    def get_slot_names(self): ...
    def variables(self): ...
