# Stubs for tensorflow.contrib.tensor_forest.python.ops.model_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.tensor_forest.python.ops import gen_model_ops as gen_model_ops
from tensorflow.contrib.tensor_forest.python.ops.gen_model_ops import feature_usage_counts as feature_usage_counts, traverse_tree_v4 as traverse_tree_v4, tree_predictions_v4 as tree_predictions_v4, tree_size as tree_size, update_model_v4 as update_model_v4
from tensorflow.contrib.util import loader as loader
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import resources as resources
from tensorflow.python.platform import resource_loader as resource_loader
from tensorflow.python.training import saver as saver
from typing import Any as Any, Optional as Optional

class TreeVariableSavable(saver.BaseSaverBuilder.SaveableObject):
    params: Any = ...
    def __init__(self, params: Any, tree_handle: Any, stats_handle: Any, create_op: Any, name: Any) -> None: ...
    def restore(self, restored_tensors: Any, unused_restored_shapes: Any): ...

def tree_variable(params: Any, tree_config: Any, stats_handle: Any, name: Any, container: Optional[Any] = ...): ...
