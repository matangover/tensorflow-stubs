# Stubs for tensorflow.contrib.boosted_trees.python.ops.stats_accumulator_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.boosted_trees.python.ops import batch_ops_utils as batch_ops_utils, boosted_trees_ops_loader as boosted_trees_ops_loader, gen_stats_accumulator_ops as gen_stats_accumulator_ops
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import resources as resources
from tensorflow.python.training import saver as saver
from typing import Any as Any, Optional as Optional

class StatsAccumulator(saver.BaseSaverBuilder.SaveableObject):
    def __init__(self, stamp_token: Any, gradient_shape: Any, hessian_shape: Any, name: Optional[Any] = ..., container: Optional[Any] = ...) -> None: ...
    def add(self, stamp_token: Any, partition_ids: Any, feature_ids: Any, gradients: Any, hessians: Any): ...
    def schedule_add(self, partition_ids: Any, feature_ids: Any, gradients: Any, hessians: Any): ...
    def deserialize(self, stamp_token: Any, num_updates: Any, partition_ids: Any, feature_ids: Any, gradients: Any, hessians: Any): ...
    def flush(self, stamp_token: Any, next_stamp_token: Any): ...
    def serialize(self): ...
    def restore(self, restored_tensors: Any, unused_restored_shapes: Any): ...
    def resource(self): ...
