# Stubs for tensorflow.python.keras.layers.cudnn_recurrent (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op
from tensorflow.python.keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import InputSpec as InputSpec
from tensorflow.python.keras.layers.recurrent import RNN as RNN
from tensorflow.python.ops import array_ops as array_ops, gen_cudnn_rnn_ops as gen_cudnn_rnn_ops, state_ops as state_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class _CuDNNRNN(RNN):
    return_sequences: Any = ...
    return_state: Any = ...
    go_backwards: Any = ...
    stateful: Any = ...
    supports_masking: bool = ...
    input_spec: Any = ...
    state_spec: Any = ...
    constants_spec: Any = ...
    def __init__(self, return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, mask: Optional[Any] = ..., training: Optional[Any] = ..., initial_state: Optional[Any] = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def losses(self): ...
    def get_losses_for(self, inputs: Optional[Any] = ...): ...

class CuDNNGRU(_CuDNNRNN):
    units: Any = ...
    kernel_initializer: Any = ...
    recurrent_initializer: Any = ...
    bias_initializer: Any = ...
    kernel_regularizer: Any = ...
    recurrent_regularizer: Any = ...
    bias_regularizer: Any = ...
    activity_regularizer: Any = ...
    kernel_constraint: Any = ...
    recurrent_constraint: Any = ...
    bias_constraint: Any = ...
    def __init__(self, units: Any, kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., **kwargs: Any) -> None: ...
    @property
    def cell(self): ...
    kernel: Any = ...
    recurrent_kernel: Any = ...
    bias: Any = ...
    built: bool = ...
    def build(self, input_shape: Any) -> None: ...
    def get_config(self): ...

class CuDNNLSTM(_CuDNNRNN):
    units: Any = ...
    kernel_initializer: Any = ...
    recurrent_initializer: Any = ...
    bias_initializer: Any = ...
    unit_forget_bias: Any = ...
    kernel_regularizer: Any = ...
    recurrent_regularizer: Any = ...
    bias_regularizer: Any = ...
    activity_regularizer: Any = ...
    kernel_constraint: Any = ...
    recurrent_constraint: Any = ...
    bias_constraint: Any = ...
    def __init__(self, units: Any, kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., unit_forget_bias: bool = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., **kwargs: Any) -> None: ...
    @property
    def cell(self): ...
    kernel: Any = ...
    recurrent_kernel: Any = ...
    bias: Any = ...
    built: bool = ...
    def build(self, input_shape: Any): ...
    def get_config(self): ...