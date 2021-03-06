# Stubs for tensorflow.contrib.boosted_trees.lib.learner.batch.ordinal_split_handler (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.contrib.boosted_trees.lib.learner.batch import base_split_handler as base_split_handler
from tensorflow.contrib.boosted_trees.proto import learner_pb2 as learner_pb2
from tensorflow.contrib.boosted_trees.python.ops import gen_quantile_ops as gen_quantile_ops, gen_stats_accumulator_ops as gen_stats_accumulator_ops, quantile_ops as quantile_ops, split_handler_ops as split_handler_ops, stats_accumulator_ops as stats_accumulator_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, function as function, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

class InequalitySplitHandler(base_split_handler.BaseSplitHandler, metaclass=abc.ABCMeta):
    def __init__(self, l1_regularization: Any, l2_regularization: Any, tree_complexity_regularization: Any, min_node_weight: Any, feature_column_group_id: Any, epsilon: Any, num_quantiles: Any, gradient_shape: Any, hessian_shape: Any, multiclass_strategy: Any, init_stamp_token: int = ..., loss_uses_sum_reduction: bool = ..., name: Optional[Any] = ...) -> None: ...
    def reset(self, stamp_token: Any, next_stamp_token: Any): ...

class DenseSplitHandler(InequalitySplitHandler):
    def __init__(self, dense_float_column: Any, l1_regularization: Any, l2_regularization: Any, tree_complexity_regularization: Any, min_node_weight: Any, feature_column_group_id: Any, epsilon: Any, num_quantiles: Any, gradient_shape: Any, hessian_shape: Any, multiclass_strategy: Any, init_stamp_token: int = ..., loss_uses_sum_reduction: bool = ..., weak_learner_type: Any = ..., name: Optional[Any] = ...) -> None: ...
    def scheduled_reads(self): ...
    def update_stats(self, stamp_token: Any, example_partition_ids: Any, gradients: Any, hessians: Any, empty_gradients: Any, empty_hessians: Any, weights: Any, is_active: Any, scheduled_reads: Any): ...
    def make_splits(self, stamp_token: Any, next_stamp_token: Any, class_id: Any): ...

class SparseSplitHandler(InequalitySplitHandler):
    def __init__(self, sparse_float_column: Any, l1_regularization: Any, l2_regularization: Any, tree_complexity_regularization: Any, min_node_weight: Any, feature_column_group_id: Any, epsilon: Any, num_quantiles: Any, gradient_shape: Any, hessian_shape: Any, multiclass_strategy: Any, init_stamp_token: int = ..., loss_uses_sum_reduction: bool = ..., name: Optional[Any] = ...) -> None: ...
    def scheduled_reads(self): ...
    def update_stats(self, stamp_token: Any, example_partition_ids: Any, gradients: Any, hessians: Any, empty_gradients: Any, empty_hessians: Any, weights: Any, is_active: Any, scheduled_reads: Any): ...
    def make_splits(self, stamp_token: Any, next_stamp_token: Any, class_id: Any): ...

make_dense_split_scalar: Any
make_dense_split_tensor: Any
make_sparse_split_scalar: Any
make_sparse_split_tensor: Any

def dense_make_stats_update(is_active: Any, are_buckets_ready: Any, float_column: Any, quantile_buckets: Any, example_partition_ids: Any, gradients: Any, hessians: Any, weights: Any, empty_gradients: Any, empty_hessians: Any): ...
def sparse_make_stats_update(is_active: Any, are_buckets_ready: Any, sparse_column_indices: Any, sparse_column_values: Any, sparse_column_shape: Any, quantile_buckets: Any, example_partition_ids: Any, gradients: Any, hessians: Any, weights: Any, empty_gradients: Any, empty_hessians: Any): ...
