# Stubs for tensorflow.contrib.estimator.python.estimator.replicate_model_fn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import node_def_pb2 as node_def_pb2
from tensorflow.python.client import device_lib as device_lib
from tensorflow.python.framework import sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, sparse_ops as sparse_ops, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.ops.losses import losses as losses
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.training import optimizer as optimizer_lib
from tensorflow.python.util import deprecation as deprecation, function_utils as function_utils
from typing import Any as Any, Optional as Optional

def replicate_model_fn(model_fn: Any, loss_reduction: Any = ..., devices: Optional[Any] = ...): ...

class _VariableDistributionMode:
    SHARED_LOCAL_PARAMETER_SERVER: int = ...
    SHARED_ROUND_ROBIN: int = ...

class TowerOptimizer(optimizer_lib.Optimizer):
    COLLECTION_FOR_GRAPH_STATES: str = ...
    def __init__(self, optimizer_or_optimizer_fn: Any) -> None: ...
    @staticmethod
    def has_been_used(): ...
    def get_slot(self, *args: Any, **kwargs: Any): ...
    def get_slot_names(self, *args: Any, **kwargs: Any): ...
    def get_name(self, *args: Any, **kwargs: Any): ...
    def variables(self, *args: Any, **kwargs: Any): ...
    def compute_gradients(self, loss: Any, *args: Any, **kwargs: Any): ...
    def apply_gradients(self, grads_and_vars: Any, global_step: Optional[Any] = ..., **kwargs: Any): ...
    class _PerGraphState:
        def __init__(self) -> None: ...
        def collect_gradients(self, grads_and_vars: Any) -> None: ...
        def get_latest_gradients_from_all_towers(self): ...
        def set_reduction_across_towers(self, loss_reduction: Any, number_of_towers: Any) -> None: ...
        def tower(self, tower_id: Any, var_scope: Any, name_scope: Any) -> None: ...
        @property
        def scopes_of_the_first_tower(self): ...
        @property
        def is_the_last_tower(self): ...
        @property
        def number_of_towers(self): ...
        @property
        def loss_reduction(self): ...
        @property
        def has_tower_optimizer_been_used(self): ...
        @has_tower_optimizer_been_used.setter
        def has_tower_optimizer_been_used(self, value: Any) -> None: ...
        def did_towers_have_same_optimizer_calls(self): ...
