# Stubs for tensorflow.python.ops.rnn_cell_impl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.keras import activations as activations, initializers as initializers
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.layers import base as base_layer
from tensorflow.python.ops import array_ops as array_ops, clip_ops as clip_ops, init_ops as init_ops, math_ops as math_ops, nn_ops as nn_ops, partitioned_variables as partitioned_variables, random_ops as random_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

ASSERT_LIKE_RNNCELL_ERROR_REGEXP: str

def assert_like_rnncell(cell_name: Any, cell: Any) -> None: ...

class RNNCell(base_layer.Layer):
    def __init__(self, trainable: bool = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def __call__(self, inputs: Any, state: Any, scope: Optional[Any] = ...): ...
    @property
    def state_size(self) -> None: ...
    @property
    def output_size(self) -> None: ...
    def build(self, _: Any) -> None: ...
    def get_initial_state(self, inputs: Optional[Any] = ..., batch_size: Optional[Any] = ..., dtype: Optional[Any] = ...): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...

class LayerRNNCell(RNNCell):
    def __call__(self, inputs: Any, state: Any, scope: Optional[Any] = ..., *args: Any, **kwargs: Any): ...

class BasicRNNCell(LayerRNNCell):
    input_spec: Any = ...
    def __init__(self, num_units: Any, activation: Optional[Any] = ..., reuse: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool = ...
    def build(self, inputs_shape: Any) -> None: ...
    def call(self, inputs: Any, state: Any): ...
    def get_config(self): ...

class GRUCell(LayerRNNCell):
    input_spec: Any = ...
    def __init__(self, num_units: Any, activation: Optional[Any] = ..., reuse: Optional[Any] = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool = ...
    def build(self, inputs_shape: Any) -> None: ...
    def call(self, inputs: Any, state: Any): ...
    def get_config(self): ...

_LSTMStateTuple = namedtuple('LSTMStateTuple', ['c', 'h'])

class LSTMStateTuple(_LSTMStateTuple):
    @property
    def dtype(self): ...

class BasicLSTMCell(LayerRNNCell):
    input_spec: Any = ...
    def __init__(self, num_units: Any, forget_bias: float = ..., state_is_tuple: bool = ..., activation: Optional[Any] = ..., reuse: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool = ...
    def build(self, inputs_shape: Any) -> None: ...
    def call(self, inputs: Any, state: Any): ...
    def get_config(self): ...

class LSTMCell(LayerRNNCell):
    input_spec: Any = ...
    def __init__(self, num_units: Any, use_peepholes: bool = ..., cell_clip: Optional[Any] = ..., initializer: Optional[Any] = ..., num_proj: Optional[Any] = ..., proj_clip: Optional[Any] = ..., num_unit_shards: Optional[Any] = ..., num_proj_shards: Optional[Any] = ..., forget_bias: float = ..., state_is_tuple: bool = ..., activation: Optional[Any] = ..., reuse: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool = ...
    def build(self, inputs_shape: Any) -> None: ...
    def call(self, inputs: Any, state: Any): ...
    def get_config(self): ...

class DropoutWrapper(RNNCell):
    def __init__(self, cell: Any, input_keep_prob: float = ..., output_keep_prob: float = ..., state_keep_prob: float = ..., variational_recurrent: bool = ..., input_size: Optional[Any] = ..., dtype: Optional[Any] = ..., seed: Optional[Any] = ..., dropout_state_filter_visitor: Optional[Any] = ...) -> None: ...
    @property
    def wrapped_cell(self): ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...
    def __call__(self, inputs: Any, state: Any, scope: Optional[Any] = ...): ...

class ResidualWrapper(RNNCell):
    def __init__(self, cell: Any, residual_fn: Optional[Any] = ...) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...
    def __call__(self, inputs: Any, state: Any, scope: Optional[Any] = ...): ...

class DeviceWrapper(RNNCell):
    def __init__(self, cell: Any, device: Any) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...
    def __call__(self, inputs: Any, state: Any, scope: Optional[Any] = ...): ...

class MultiRNNCell(RNNCell):
    def __init__(self, cells: Any, state_is_tuple: bool = ...) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...
    def call(self, inputs: Any, state: Any): ...
