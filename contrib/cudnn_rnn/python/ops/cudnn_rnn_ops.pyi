# Stubs for tensorflow.contrib.cudnn_rnn.python.ops.cudnn_rnn_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.checkpoint.python import split_dependency as split_dependency
from tensorflow.contrib.rnn.python.ops import lstm_ops as lstm_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, random_seed as random_seed
from tensorflow.python.keras.engine import base_layer as base_layer
from tensorflow.python.ops import array_ops as array_ops, gen_cudnn_rnn_ops as gen_cudnn_rnn_ops, init_ops as init_ops, math_ops as math_ops, nn_ops as nn_ops, rnn_cell_impl as rnn_cell_impl, state_ops as state_ops
from tensorflow.python.training import saver as saver
from typing import Any as Any, Optional as Optional

CUDNN_RNN_UNIDIRECTION: str
CUDNN_RNN_BIDIRECTION: str
CUDNN_LSTM: str
CUDNN_GRU: str
CUDNN_RNN_RELU: str
CUDNN_RNN_TANH: str
CUDNN_LSTM_PARAMS_PER_LAYER: int
CUDNN_GRU_PARAMS_PER_LAYER: int
CUDNN_RNN_TANH_PARAMS_PER_LAYER: int
CUDNN_RNN_RELU_PARAMS_PER_LAYER: int
CUDNN_INPUT_LINEAR_MODE: str
CUDNN_INPUT_SKIP_MODE: str
CUDNN_INPUT_AUTO_MODE: str

class CudnnCompatibleLSTMCell(lstm_ops.LSTMBlockCell):
    def __init__(self, num_units: Any, reuse: Optional[Any] = ...) -> None: ...

class CudnnCompatibleGRUCell(rnn_cell_impl.GRUCell):
    def __init__(self, num_units: Any, reuse: Optional[Any] = ..., kernel_initializer: Optional[Any] = ...) -> None: ...
    def build(self, inputs_shape: Any) -> None: ...
    def call(self, inputs: Any, state: Any): ...

class CudnnOpaqueParamsSaveable(saver.BaseSaverBuilder.SaveableObject):
    def __init__(self, opaque_params: Any, num_layers: Any, num_units: Any, input_size: Any, input_mode: Any = ..., direction: Any = ..., scope: Optional[Any] = ..., name: str = ...) -> None: ...
    def restore(self, restored_tensors: Any, restored_shapes: Any): ...

class CudnnLSTMSaveable(CudnnOpaqueParamsSaveable): ...
class CudnnGRUSaveable(CudnnOpaqueParamsSaveable): ...
class CudnnRNNSimpleSaveable(CudnnLSTMSaveable): ...
class CudnnRNNTanhSaveable(CudnnRNNSimpleSaveable): ...
class CudnnRNNReluSaveable(CudnnRNNSimpleSaveable): ...

def check_direction(direction: Any) -> None: ...
def check_input_mode(input_mode: Any) -> None: ...
def cudnn_lstm(inputs: Any, input_h: Any, input_c: Any, params: Any, is_training: Any, input_mode: Any = ..., direction: Any = ..., dropout: float = ..., seed: int = ..., name: Optional[Any] = ...): ...
def cudnn_gru(inputs: Any, input_h: Any, params: Any, is_training: Any, input_mode: Any = ..., direction: Any = ..., dropout: float = ..., seed: int = ..., name: Optional[Any] = ...): ...
def cudnn_rnn_relu(inputs: Any, input_h: Any, params: Any, is_training: Any, input_mode: Any = ..., direction: Any = ..., dropout: float = ..., seed: int = ..., name: Optional[Any] = ...): ...
def cudnn_rnn_tanh(inputs: Any, input_h: Any, params: Any, is_training: Any, input_mode: Any = ..., direction: Any = ..., dropout: float = ..., seed: int = ..., name: Optional[Any] = ...): ...
def cudnn_rnn_opaque_params_to_canonical(rnn_mode: Any, num_layers: Any, num_units: Any, input_size: Any, params: Any, input_mode: Any = ..., direction: Any = ..., dropout: int = ..., seed: int = ..., name: Optional[Any] = ...): ...
def cudnn_rnn_canonical_to_opaque_params(rnn_mode: Any, num_layers: Any, num_units: Any, input_size: Any, weights: Any, biases: Any, input_mode: Any = ..., direction: Any = ..., dropout: int = ..., seed: int = ..., name: Optional[Any] = ...): ...
def cudnn_rnn_opaque_params_size(rnn_mode: Any, num_layers: Any, num_units: Any, input_size: Any, input_mode: Any = ..., direction: Any = ..., dtype: Any = ..., dropout: int = ..., seed: int = ..., name: Optional[Any] = ...): ...

class _CudnnRNN:
    def __init__(self, rnn_mode: Any, num_layers: Any, num_units: Any, input_size: Any, input_mode: Any = ..., direction: Any = ..., dtype: Any = ..., dropout: float = ..., seed: int = ...) -> None: ...
    @property
    def input_mode(self): ...
    @property
    def input_size(self): ...
    @property
    def num_units(self): ...
    @property
    def num_layers(self): ...
    @property
    def rnn_mode(self): ...
    @property
    def direction(self): ...
    def params_size(self): ...
    def __call__(self, input_data: Any, input_h: Any, input_c: Any, params: Any, is_training: bool = ...): ...
    def params_to_canonical(self, params: Any): ...
    def canonical_to_params(self, weights: Any, biases: Any): ...

class CudnnLSTM(_CudnnRNN):
    def __init__(self, num_layers: Any, num_units: Any, input_size: Any, input_mode: Any = ..., direction: Any = ..., dtype: Any = ..., dropout: float = ..., seed: int = ...) -> None: ...
    def __call__(self, input_data: Any, input_h: Any, input_c: Any, params: Any, is_training: bool = ...): ...

class _CudnnRNNNoInputC(_CudnnRNN):
    def __init__(self, num_layers: Any, num_units: Any, input_size: Any, input_mode: Any = ..., direction: Any = ..., dtype: Any = ..., dropout: float = ..., seed: int = ...) -> None: ...
    def __call__(self, input_data: Any, input_h: Any, params: Any, is_training: bool = ...): ...

class CudnnGRU(_CudnnRNNNoInputC): ...
class CudnnRNNTanh(_CudnnRNNNoInputC): ...
class CudnnRNNRelu(_CudnnRNNNoInputC): ...
