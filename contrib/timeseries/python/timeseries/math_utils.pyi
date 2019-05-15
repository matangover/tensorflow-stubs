# Stubs for tensorflow.contrib.timeseries.python.timeseries.math_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.contrib import lookup as lookup
from tensorflow.contrib.layers.python.layers import layers as layers
from tensorflow.contrib.timeseries.python.timeseries.feature_keys import TrainEvalFeatures as TrainEvalFeatures
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, functional_ops as functional_ops, gen_math_ops as gen_math_ops, init_ops as init_ops, linalg_ops as linalg_ops, math_ops as math_ops, nn as nn, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

def clip_covariance(covariance_matrix: Any, maximum_variance_ratio: Any, minimum_variance: Any): ...
def block_diagonal(matrices: Any, dtype: Any = ..., name: str = ...): ...
def power_sums_tensor(array_size: Any, power_matrix: Any, multiplier: Any): ...
def matrix_to_powers(matrix: Any, powers: Any): ...
def batch_matrix_pow(matrices: Any, powers: Any): ...
def batch_times_matrix(batch: Any, matrix: Any, adj_x: bool = ..., adj_y: bool = ...): ...
def matrix_times_batch(matrix: Any, batch: Any, adj_x: bool = ..., adj_y: bool = ...): ...
def make_toeplitz_matrix(inputs: Any, name: Optional[Any] = ...): ...
def sign_magnitude_positive_definite(raw: Any, off_diagonal_scale: float = ..., overall_scale: float = ...): ...
def transform_to_covariance_matrices(input_vectors: Any, matrix_size: Any): ...
def variable_covariance_matrix(size: Any, name: Any, dtype: Any, initial_diagonal_values: Optional[Any] = ..., initial_overall_scale_log: float = ...): ...
def batch_start_time(times: Any): ...
def batch_end_time(times: Any): ...
def log_noninformative_covariance_prior(covariance: Any): ...
def entropy_matched_cauchy_scale(covariance: Any): ...

class TensorValuedMutableDenseHashTable(lookup.MutableDenseHashTable):
    def __init__(self, key_dtype: Any, value_dtype: Any, default_value: Any, *args: Any, **kwargs: Any) -> None: ...
    def insert(self, keys: Any, values: Any, name: Optional[Any] = ...): ...
    def lookup(self, keys: Any, name: Optional[Any] = ...): ...

class TupleOfTensorsLookup(lookup.LookupInterface):
    def __init__(self, key_dtype: Any, default_values: Any, empty_key: Any, name: Any, checkpoint: bool = ...) -> None: ...
    def lookup(self, keys: Any): ...
    def insert(self, keys: Any, values: Any): ...
    def check_table_dtypes(self, key_dtype: Any, value_dtype: Any) -> None: ...

def replicate_state(start_state: Any, batch_size: Any): ...

Moments = namedtuple('Moments', ['mean', 'variance'])

InputStatistics = namedtuple('InputStatistics', ['series_start_moments', 'overall_feature_moments', 'start_time', 'total_observation_count'])

class InputStatisticsFromMiniBatch:
    def __init__(self, num_features: Any, dtype: Any, starting_variance_window_size: int = ...) -> None: ...
    def initialize_graph(self, features: Any, update_statistics: bool = ...): ...
    class _AdaptiveInputAuxiliaryStatistics:
        def __new__(cls, num_features: Any, dtype: Any): ...
