# Stubs for tensorflow.python.keras.layers.convolutional_recurrent (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.keras import activations as activations, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import InputSpec as InputSpec, Layer as Layer
from tensorflow.python.keras.layers.recurrent import RNN as RNN, _generate_dropout_mask as _generate_dropout_mask, _standardize_args as _standardize_args
from tensorflow.python.keras.utils import conv_utils as conv_utils, generic_utils as generic_utils, tf_utils as tf_utils
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class ConvRNN2D(RNN):
    input_spec: Any = ...
    states: Any = ...
    def __init__(self, cell: Any, return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., unroll: bool = ..., **kwargs: Any) -> None: ...
    def compute_output_shape(self, input_shape: Any): ...
    state_spec: Any = ...
    built: bool = ...
    def build(self, input_shape: Any) -> None: ...
    def get_initial_state(self, inputs: Any): ...
    constants_spec: Any = ...
    def __call__(self, inputs: Any, initial_state: Optional[Any] = ..., constants: Optional[Any] = ..., **kwargs: Any): ...
    def call(self, inputs: Any, mask: Optional[Any] = ..., training: Optional[Any] = ..., initial_state: Optional[Any] = ..., constants: Optional[Any] = ...): ...
    def reset_states(self, states: Optional[Any] = ...): ...

class ConvLSTM2DCell(Layer):
    filters: Any = ...
    kernel_size: Any = ...
    strides: Any = ...
    padding: Any = ...
    data_format: Any = ...
    dilation_rate: Any = ...
    activation: Any = ...
    recurrent_activation: Any = ...
    use_bias: Any = ...
    kernel_initializer: Any = ...
    recurrent_initializer: Any = ...
    bias_initializer: Any = ...
    unit_forget_bias: Any = ...
    kernel_regularizer: Any = ...
    recurrent_regularizer: Any = ...
    bias_regularizer: Any = ...
    kernel_constraint: Any = ...
    recurrent_constraint: Any = ...
    bias_constraint: Any = ...
    dropout: Any = ...
    recurrent_dropout: Any = ...
    state_size: Any = ...
    def __init__(self, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: Optional[Any] = ..., dilation_rate: Any = ..., activation: str = ..., recurrent_activation: str = ..., use_bias: bool = ..., kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., unit_forget_bias: bool = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., dropout: float = ..., recurrent_dropout: float = ..., **kwargs: Any) -> None: ...
    kernel_shape: Any = ...
    kernel: Any = ...
    recurrent_kernel: Any = ...
    bias: Any = ...
    kernel_i: Any = ...
    recurrent_kernel_i: Any = ...
    kernel_f: Any = ...
    recurrent_kernel_f: Any = ...
    kernel_c: Any = ...
    recurrent_kernel_c: Any = ...
    kernel_o: Any = ...
    recurrent_kernel_o: Any = ...
    bias_i: Any = ...
    bias_f: Any = ...
    bias_c: Any = ...
    bias_o: Any = ...
    built: bool = ...
    def build(self, input_shape: Any): ...
    def call(self, inputs: Any, states: Any, training: Optional[Any] = ...): ...
    def input_conv(self, x: Any, w: Any, b: Optional[Any] = ..., padding: str = ...): ...
    def recurrent_conv(self, x: Any, w: Any): ...
    def get_config(self): ...

class ConvLSTM2D(ConvRNN2D):
    activity_regularizer: Any = ...
    def __init__(self, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: Optional[Any] = ..., dilation_rate: Any = ..., activation: str = ..., recurrent_activation: str = ..., use_bias: bool = ..., kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., unit_forget_bias: bool = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., return_sequences: bool = ..., go_backwards: bool = ..., stateful: bool = ..., dropout: float = ..., recurrent_dropout: float = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, mask: Optional[Any] = ..., training: Optional[Any] = ..., initial_state: Optional[Any] = ...): ...
    @property
    def filters(self): ...
    @property
    def kernel_size(self): ...
    @property
    def strides(self): ...
    @property
    def padding(self): ...
    @property
    def data_format(self): ...
    @property
    def dilation_rate(self): ...
    @property
    def activation(self): ...
    @property
    def recurrent_activation(self): ...
    @property
    def use_bias(self): ...
    @property
    def kernel_initializer(self): ...
    @property
    def recurrent_initializer(self): ...
    @property
    def bias_initializer(self): ...
    @property
    def unit_forget_bias(self): ...
    @property
    def kernel_regularizer(self): ...
    @property
    def recurrent_regularizer(self): ...
    @property
    def bias_regularizer(self): ...
    @property
    def kernel_constraint(self): ...
    @property
    def recurrent_constraint(self): ...
    @property
    def bias_constraint(self): ...
    @property
    def dropout(self): ...
    @property
    def recurrent_dropout(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any): ...