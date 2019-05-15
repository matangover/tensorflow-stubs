# Stubs for tensorflow.python.ops.sparse_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops.gen_sparse_ops import *
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_sparse_ops as gen_sparse_ops, math_ops as math_ops
from tensorflow.python.util import compat as compat, deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def sparse_expand_dims(sp_input: Any, axis: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sparse_eye(num_rows: Any, num_columns: Optional[Any] = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def sparse_concat(axis: Any, sp_inputs: Any, name: Optional[Any] = ..., expand_nonconcat_dim: bool = ..., concat_dim: Optional[Any] = ...): ...
def sparse_add(a: Any, b: Any, thresh: int = ...): ...
def sparse_cross(inputs: Any, name: Optional[Any] = ...): ...
def sparse_cross_hashed(inputs: Any, num_buckets: int = ..., hash_key: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sparse_dense_cwise_add(sp_t: Any, dense_t: Any): ...
def sparse_reorder(sp_input: Any, name: Optional[Any] = ...): ...
def sparse_reshape(sp_input: Any, shape: Any, name: Optional[Any] = ...): ...

class KeywordRequired: ...

def sparse_split(keyword_required: Any = ..., sp_input: Optional[Any] = ..., num_split: Optional[Any] = ..., axis: Optional[Any] = ..., name: Optional[Any] = ..., split_dim: Optional[Any] = ...): ...
def sparse_slice(sp_input: Any, start: Any, size: Any, name: Optional[Any] = ...): ...
def sparse_to_dense(sparse_indices: Any, output_shape: Any, sparse_values: Any, default_value: int = ..., validate_indices: bool = ..., name: Optional[Any] = ...): ...
def sparse_reduce_max(sp_input: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., reduction_axes: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def sparse_reduce_max_sparse(sp_input: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., reduction_axes: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def sparse_reduce_sum(sp_input: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., reduction_axes: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def sparse_reduce_sum_sparse(sp_input: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., reduction_axes: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def sparse_tensor_to_dense(sp_input: Any, default_value: int = ..., validate_indices: bool = ..., name: Optional[Any] = ...): ...
def sparse_to_indicator(sp_input: Any, vocab_size: Any, name: Optional[Any] = ...): ...
def sparse_merge(sp_ids: Any, sp_values: Any, vocab_size: Any, name: Optional[Any] = ..., already_sorted: bool = ...): ...
def sparse_retain(sp_input: Any, to_retain: Any): ...
def sparse_reset_shape(sp_input: Any, new_shape: Optional[Any] = ...): ...
def sparse_fill_empty_rows(sp_input: Any, default_value: Any, name: Optional[Any] = ...): ...
def serialize_sparse(sp_input: Any, name: Optional[Any] = ..., out_type: Any = ...): ...
def serialize_many_sparse(sp_input: Any, name: Optional[Any] = ..., out_type: Any = ...): ...
def deserialize_sparse(serialized_sparse: Any, dtype: Any, rank: Optional[Any] = ..., name: Optional[Any] = ...): ...
def deserialize_many_sparse(serialized_sparse: Any, dtype: Any, rank: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sparse_tensor_dense_matmul(sp_a: Any, b: Any, adjoint_a: bool = ..., adjoint_b: bool = ..., name: Optional[Any] = ...): ...
def sparse_softmax(sp_input: Any, name: Optional[Any] = ...): ...
def sparse_maximum(sp_a: Any, sp_b: Any, name: Optional[Any] = ...): ...
def sparse_minimum(sp_a: Any, sp_b: Any, name: Optional[Any] = ...): ...
def sparse_transpose(sp_input: Any, perm: Optional[Any] = ..., name: Optional[Any] = ...): ...
