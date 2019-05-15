# Stubs for tensorflow.contrib.tensor_forest.python.ops.stats_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.tensor_forest.python.ops import gen_stats_ops as gen_stats_ops
from tensorflow.contrib.tensor_forest.python.ops.gen_stats_ops import finalize_tree as finalize_tree, grow_tree_v4 as grow_tree_v4, process_input_v4 as process_input_v4
from tensorflow.contrib.util import loader as loader
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import resources as resources
from tensorflow.python.platform import resource_loader as resource_loader
from tensorflow.python.training import saver as saver
from typing import Any as Any, Optional as Optional

class FertileStatsVariableSavable(saver.BaseSaverBuilder.SaveableObject):
    params: Any = ...
    def __init__(self, params: Any, stats_handle: Any, create_op: Any, name: Any) -> None: ...
    def restore(self, restored_tensors: Any, unused_restored_shapes: Any): ...

def fertile_stats_variable(params: Any, stats_config: Any, name: Any, container: Optional[Any] = ...): ...