# Stubs for tensorflow.python.keras.layers.wrappers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras.engine.base_layer import InputSpec as InputSpec, Layer as Layer
from tensorflow.python.keras.layers.recurrent import _standardize_args as _standardize_args
from tensorflow.python.keras.utils import generic_utils as generic_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class Wrapper(Layer):
    layer: Any = ...
    def __init__(self, layer: Any, **kwargs: Any) -> None: ...
    built: bool = ...
    def build(self, input_shape: Optional[Any] = ...) -> None: ...
    @property
    def activity_regularizer(self): ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value: Any) -> None: ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def updates(self): ...
    @property
    def losses(self): ...
    def get_weights(self): ...
    def set_weights(self, weights: Any) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ...): ...

class TimeDistributed(Wrapper):
    supports_masking: bool = ...
    def __init__(self, layer: Any, **kwargs: Any) -> None: ...
    input_spec: Any = ...
    built: bool = ...
    def build(self, input_shape: Any) -> None: ...
    def compute_output_shape(self, input_shape: Any): ...
    def call(self, inputs: Any, training: Optional[Any] = ..., mask: Optional[Any] = ...): ...
    def compute_mask(self, inputs: Any, mask: Optional[Any] = ...): ...

class Bidirectional(Wrapper):
    forward_layer: Any = ...
    backward_layer: Any = ...
    merge_mode: Any = ...
    stateful: Any = ...
    return_sequences: Any = ...
    return_state: Any = ...
    supports_masking: bool = ...
    input_spec: Any = ...
    def __init__(self, layer: Any, merge_mode: str = ..., weights: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value: Any) -> None: ...
    def get_weights(self): ...
    def set_weights(self, weights: Any) -> None: ...
    def compute_output_shape(self, input_shape: Any): ...
    def __call__(self, inputs: Any, initial_state: Optional[Any] = ..., constants: Optional[Any] = ..., **kwargs: Any): ...
    def call(self, inputs: Any, training: Optional[Any] = ..., mask: Optional[Any] = ..., initial_state: Optional[Any] = ..., constants: Optional[Any] = ...): ...
    def reset_states(self) -> None: ...
    built: bool = ...
    def build(self, input_shape: Any) -> None: ...
    def compute_mask(self, inputs: Any, mask: Any): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def updates(self): ...
    @property
    def losses(self): ...
    @property
    def constraints(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ...): ...
