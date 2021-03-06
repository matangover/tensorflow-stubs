# Stubs for tensorflow.contrib.model_pruning.python.pruning (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.model_pruning.python import pruning_utils as pruning_utils
from tensorflow.contrib.training.python.training import hparam as hparam
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, nn_impl as nn_impl, nn_ops as nn_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import training_util as training_util
from typing import Any as Any, Optional as Optional

def apply_mask(x: Any, scope: str = ...): ...
def get_masked_weights(): ...
def get_masks(): ...
def get_thresholds(): ...
def get_weights(): ...
def get_weight_sparsity(): ...
def get_pruning_hparams(): ...

class Pruning:
    def __init__(self, spec: Optional[Any] = ..., global_step: Optional[Any] = ..., sparsity: Optional[Any] = ...) -> None: ...
    def mask_update_op(self): ...
    def conditional_mask_update_op(self): ...
    def add_pruning_summaries(self) -> None: ...
    def print_hparams(self) -> None: ...
