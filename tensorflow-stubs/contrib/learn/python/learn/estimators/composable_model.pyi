# Stubs for tensorflow.contrib.learn.python.learn.estimators.composable_model (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib import layers as layers
from tensorflow.contrib.framework import list_variables as list_variables, load_variable as load_variable
from tensorflow.contrib.layers.python.layers import feature_column_ops as feature_column_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import clip_ops as clip_ops, gradients as gradients, nn as nn, partitioned_variables as partitioned_variables, variable_scope as variable_scope
from tensorflow.python.summary import summary as summary
from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any as Any, Optional as Optional

class _ComposableModel:
    def __init__(self, num_label_columns: Any, optimizer: Any, gradient_clip_norm: Any, num_ps_replicas: Any, scope: Any, trainable: bool = ...) -> None: ...
    def get_scope_name(self): ...
    def build_model(self, features: Any, feature_columns: Any, is_training: Any) -> None: ...
    def get_train_step(self, loss: Any): ...

class LinearComposableModel(_ComposableModel):
    def __init__(self, num_label_columns: Any, optimizer: Optional[Any] = ..., _joint_weights: bool = ..., gradient_clip_norm: Optional[Any] = ..., num_ps_replicas: int = ..., scope: Optional[Any] = ..., trainable: bool = ...) -> None: ...
    def get_weights(self, model_dir: Any): ...
    def get_bias(self, model_dir: Any): ...
    def build_model(self, features: Any, feature_columns: Any, is_training: Any): ...

class DNNComposableModel(_ComposableModel):
    def __init__(self, num_label_columns: Any, hidden_units: Any, optimizer: Optional[Any] = ..., activation_fn: Any = ..., dropout: Optional[Any] = ..., gradient_clip_norm: Optional[Any] = ..., num_ps_replicas: int = ..., scope: Optional[Any] = ..., trainable: bool = ...) -> None: ...
    def get_weights(self, model_dir: Any): ...
    def get_bias(self, model_dir: Any): ...
    def build_model(self, features: Any, feature_columns: Any, is_training: Any): ...