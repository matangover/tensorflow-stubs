# Stubs for tensorflow.contrib.layers.python.layers.embedding_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.layers.python.ops import sparse_feature_cross_op as sparse_feature_cross_op
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, clip_ops as clip_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, embedding_ops as embedding_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops, sparse_ops as sparse_ops, variables as variables
from typing import Any as Any, Optional as Optional

def safe_embedding_lookup_sparse(embedding_weights: Any, sparse_ids: Any, sparse_weights: Optional[Any] = ..., combiner: Optional[Any] = ..., default_id: Optional[Any] = ..., name: Optional[Any] = ..., partition_strategy: str = ..., max_norm: Optional[Any] = ...): ...
def scattered_embedding_lookup(params: Any, values: Any, dimension: Any, name: Optional[Any] = ..., hash_key: Optional[Any] = ...): ...
def scattered_embedding_lookup_sparse(params: Any, sparse_values: Any, dimension: Any, combiner: Optional[Any] = ..., default_value: Optional[Any] = ..., name: Optional[Any] = ..., hash_key: Optional[Any] = ...): ...
def embedding_lookup_unique(params: Any, ids: Any, partition_strategy: str = ..., name: Optional[Any] = ...): ...
def embedding_lookup_sparse_with_distributed_aggregation(params: Any, sp_ids: Any, sp_weights: Any, partition_strategy: str = ..., name: Optional[Any] = ..., combiner: Optional[Any] = ..., max_norm: Optional[Any] = ...): ...
