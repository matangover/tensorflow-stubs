# Stubs for tensorflow.python.keras.layers.normalization (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import InputSpec as InputSpec, Layer as Layer
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, math_ops as math_ops, nn as nn, state_ops as state_ops
from tensorflow.python.training import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class BatchNormalization(Layer):
    axis: Any = ...
    momentum: Any = ...
    epsilon: Any = ...
    center: Any = ...
    scale: Any = ...
    beta_initializer: Any = ...
    gamma_initializer: Any = ...
    moving_mean_initializer: Any = ...
    moving_variance_initializer: Any = ...
    beta_regularizer: Any = ...
    gamma_regularizer: Any = ...
    beta_constraint: Any = ...
    gamma_constraint: Any = ...
    renorm: Any = ...
    virtual_batch_size: Any = ...
    adjustment: Any = ...
    supports_masking: bool = ...
    fused: Any = ...
    renorm_clipping: Any = ...
    renorm_momentum: Any = ...
    def __init__(self, axis: int = ..., momentum: float = ..., epsilon: float = ..., center: bool = ..., scale: bool = ..., beta_initializer: str = ..., gamma_initializer: str = ..., moving_mean_initializer: str = ..., moving_variance_initializer: str = ..., beta_regularizer: Optional[Any] = ..., gamma_regularizer: Optional[Any] = ..., beta_constraint: Optional[Any] = ..., gamma_constraint: Optional[Any] = ..., renorm: bool = ..., renorm_clipping: Optional[Any] = ..., renorm_momentum: float = ..., fused: Optional[Any] = ..., trainable: bool = ..., virtual_batch_size: Optional[Any] = ..., adjustment: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    input_spec: Any = ...
    gamma: Any = ...
    beta: Any = ...
    moving_mean: Any = ...
    moving_variance: Any = ...
    renorm_mean: Any = ...
    renorm_mean_weight: Any = ...
    renorm_stddev: Any = ...
    renorm_stddev_weight: Any = ...
    built: bool = ...
    def build(self, input_shape: Any): ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...
