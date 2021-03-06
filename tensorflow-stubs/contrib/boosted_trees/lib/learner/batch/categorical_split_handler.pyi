# Stubs for tensorflow.contrib.boosted_trees.lib.learner.batch.categorical_split_handler (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.boosted_trees.lib.learner.batch import base_split_handler as base_split_handler
from tensorflow.contrib.boosted_trees.proto import learner_pb2 as learner_pb2
from tensorflow.contrib.boosted_trees.python.ops import split_handler_ops as split_handler_ops, stats_accumulator_ops as stats_accumulator_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

class EqualitySplitHandler(base_split_handler.BaseSplitHandler):
    def __init__(self, sparse_int_column: Any, l1_regularization: Any, l2_regularization: Any, tree_complexity_regularization: Any, min_node_weight: Any, feature_column_group_id: Any, gradient_shape: Any, hessian_shape: Any, multiclass_strategy: Any, init_stamp_token: int = ..., loss_uses_sum_reduction: bool = ..., weak_learner_type: Any = ..., name: Optional[Any] = ...) -> None: ...
    def update_stats(self, stamp_token: Any, example_partition_ids: Any, gradients: Any, hessians: Any, empty_gradients: Any, empty_hessians: Any, weights: Any, is_active: Any, scheduled_reads: Any): ...
    def make_splits(self, stamp_token: Any, next_stamp_token: Any, class_id: Any): ...
    def reset(self, stamp_token: Any, next_stamp_token: Any): ...
