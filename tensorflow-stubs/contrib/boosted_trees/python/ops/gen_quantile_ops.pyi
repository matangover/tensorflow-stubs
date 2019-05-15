# Stubs for tensorflow.contrib.boosted_trees.python.ops.gen_quantile_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def bucketize_with_input_boundaries(input: Any, boundaries: Any, name: Optional[Any] = ...): ...
def bucketize_with_input_boundaries_eager_fallback(input: Any, boundaries: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def create_quantile_accumulator(quantile_accumulator_handle: Any, stamp_token: Any, epsilon: Any, num_quantiles: Any, container: str = ..., shared_name: str = ..., max_elements: int = ..., generate_quantiles: bool = ..., name: Optional[Any] = ...): ...
def create_quantile_accumulator_eager_fallback(quantile_accumulator_handle: Any, stamp_token: Any, epsilon: Any, num_quantiles: Any, container: str = ..., shared_name: str = ..., max_elements: int = ..., generate_quantiles: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _MakeQuantileSummariesOutput = namedtuple('MakeQuantileSummaries', <ERROR>)

def make_quantile_summaries(dense_float_features: Any, sparse_float_feature_indices: Any, sparse_float_feature_values: Any, sparse_float_feature_shapes: Any, example_weights: Any, epsilon: Any, name: Optional[Any] = ...): ...
def make_quantile_summaries_eager_fallback(dense_float_features: Any, sparse_float_feature_indices: Any, sparse_float_feature_values: Any, sparse_float_feature_shapes: Any, example_weights: Any, epsilon: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def quantile_accumulator_add_summaries(quantile_accumulator_handles: Any, stamp_token: Any, summaries: Any, name: Optional[Any] = ...): ...
def quantile_accumulator_add_summaries_eager_fallback(quantile_accumulator_handles: Any, stamp_token: Any, summaries: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def quantile_accumulator_deserialize(quantile_accumulator_handle: Any, stamp_token: Any, stream_state: Any, are_buckets_ready: Any, buckets: Any, name: Optional[Any] = ...): ...
def quantile_accumulator_deserialize_eager_fallback(quantile_accumulator_handle: Any, stamp_token: Any, stream_state: Any, are_buckets_ready: Any, buckets: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def quantile_accumulator_flush(quantile_accumulator_handle: Any, stamp_token: Any, next_stamp_token: Any, name: Optional[Any] = ...): ...
def quantile_accumulator_flush_eager_fallback(quantile_accumulator_handle: Any, stamp_token: Any, next_stamp_token: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def quantile_accumulator_flush_summary(quantile_accumulator_handle: Any, stamp_token: Any, next_stamp_token: Any, name: Optional[Any] = ...): ...
def quantile_accumulator_flush_summary_eager_fallback(quantile_accumulator_handle: Any, stamp_token: Any, next_stamp_token: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantileAccumulatorGetBucketsOutput = namedtuple('QuantileAccumulatorGetBuckets', <ERROR>)

def quantile_accumulator_get_buckets(quantile_accumulator_handles: Any, stamp_token: Any, name: Optional[Any] = ...): ...
def quantile_accumulator_get_buckets_eager_fallback(quantile_accumulator_handles: Any, stamp_token: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def quantile_accumulator_is_initialized(quantile_accumulator_handle: Any, name: Optional[Any] = ...): ...
def quantile_accumulator_is_initialized_eager_fallback(quantile_accumulator_handle: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantileAccumulatorSerializeOutput = namedtuple('QuantileAccumulatorSerialize', <ERROR>)

def quantile_accumulator_serialize(quantile_accumulator_handle: Any, name: Optional[Any] = ...): ...
def quantile_accumulator_serialize_eager_fallback(quantile_accumulator_handle: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantileBucketsOutput = namedtuple('QuantileBuckets', <ERROR>)

def quantile_buckets(dense_float_features: Any, sparse_float_feature_indices: Any, sparse_float_feature_values: Any, sparse_float_feature_shapes: Any, example_weights: Any, dense_config: Any, sparse_config: Any, name: Optional[Any] = ...): ...
def quantile_buckets_eager_fallback(dense_float_features: Any, sparse_float_feature_indices: Any, sparse_float_feature_values: Any, sparse_float_feature_shapes: Any, example_weights: Any, dense_config: Any, sparse_config: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def quantile_stream_resource_handle_op(container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...
def quantile_stream_resource_handle_op_eager_fallback(container: str = ..., shared_name: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantilesOutput = namedtuple('Quantiles', <ERROR>)

def quantiles(dense_values: Any, sparse_values: Any, dense_buckets: Any, sparse_buckets: Any, sparse_indices: Any, name: Optional[Any] = ...): ...
def quantiles_eager_fallback(dense_values: Any, sparse_values: Any, dense_buckets: Any, sparse_buckets: Any, sparse_indices: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...