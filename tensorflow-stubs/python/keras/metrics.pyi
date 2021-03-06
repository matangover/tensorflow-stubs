# Stubs for tensorflow.python.keras.metrics (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from abc import abstractmethod as abstractmethod
from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.losses import binary_crossentropy as binary_crossentropy, categorical_crossentropy as categorical_crossentropy, cosine_proximity as cosine_proximity, hinge as hinge, kullback_leibler_divergence as kullback_leibler_divergence, logcosh as logcosh, mean_absolute_error as mean_absolute_error, mean_absolute_percentage_error as mean_absolute_percentage_error, mean_squared_error as mean_squared_error, mean_squared_logarithmic_error as mean_squared_logarithmic_error, poisson as poisson, sparse_categorical_crossentropy as sparse_categorical_crossentropy, squared_hinge as squared_hinge
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from tensorflow.python.ops import array_ops as array_ops, confusion_matrix as confusion_matrix, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, nn as nn, state_ops as state_ops, weights_broadcast_ops as weights_broadcast_ops
from tensorflow.python.training import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.util import tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any as Any, Optional as Optional

def check_is_tensor_or_operation(x: Any, name: Any) -> None: ...
def clone_metric(metric: Any): ...
def clone_metrics(metrics: Any): ...
def update_state_wrapper(update_state_fn: Any): ...
def result_wrapper(result_fn: Any): ...
def weakmethod(method: Any): ...
def safe_div(numerator: Any, denominator: Any): ...
def squeeze_or_expand_dimensions(y_pred: Any, y_true: Any, sample_weight: Any): ...

class Metric(Layer, metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    stateful: bool = ...
    built: bool = ...
    def __init__(self, name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def __new__(cls, *args: Any, **kwargs: Any): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def reset_states(self) -> None: ...
    @abstractmethod
    def update_state(self, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    def result(self) -> Any: ...
    @classmethod
    def from_config(cls, config: Any): ...
    def add_weight(self, name: Any, shape: Any = ..., aggregation: Any = ..., synchronization: Any = ..., initializer: Optional[Any] = ...): ...

class Mean(Metric):
    total: Any = ...
    count: Any = ...
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, values: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...

class MeanMetricWrapper(Mean):
    def __init__(self, fn: Any, name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def get_config(self): ...

class BinaryAccuracy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ..., threshold: float = ...) -> None: ...

class CategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class SparseCategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

def binary_accuracy(y_true: Any, y_pred: Any, threshold: float = ...): ...
def categorical_accuracy(y_true: Any, y_pred: Any): ...
def sparse_categorical_accuracy(y_true: Any, y_pred: Any): ...
def top_k_categorical_accuracy(y_true: Any, y_pred: Any, k: int = ...): ...
def sparse_top_k_categorical_accuracy(y_true: Any, y_pred: Any, k: int = ...): ...
mse = mean_squared_error
MSE = mean_squared_error
mae = mean_absolute_error
MAE = mean_absolute_error
mape = mean_absolute_percentage_error
MAPE = mean_absolute_percentage_error
msle = mean_squared_logarithmic_error
MSLE = mean_squared_logarithmic_error
cosine = cosine_proximity

def serialize(metric: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...
def get(identifier: Any): ...
