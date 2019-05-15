# Stubs for tensorflow.contrib.rnn.python.ops.core_rnn_cell (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, embedding_ops as embedding_ops, init_ops as init_ops, math_ops as math_ops, nn_ops as nn_ops, rnn_cell_impl as rnn_cell_impl
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

RNNCell = rnn_cell_impl.RNNCell

class _Linear:
    def __init__(self, args: Any, output_size: Any, build_bias: Any, bias_initializer: Optional[Any] = ..., kernel_initializer: Optional[Any] = ...) -> None: ...
    def __call__(self, args: Any): ...

class EmbeddingWrapper(RNNCell):
    def __init__(self, cell: Any, embedding_classes: Any, embedding_size: Any, initializer: Optional[Any] = ..., reuse: Optional[Any] = ...) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...
    def call(self, inputs: Any, state: Any): ...

class InputProjectionWrapper(RNNCell):
    def __init__(self, cell: Any, num_proj: Any, activation: Optional[Any] = ..., input_size: Optional[Any] = ..., reuse: Optional[Any] = ...) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...
    def call(self, inputs: Any, state: Any): ...

class OutputProjectionWrapper(RNNCell):
    def __init__(self, cell: Any, output_size: Any, activation: Optional[Any] = ..., reuse: Optional[Any] = ...) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size: Any, dtype: Any): ...
    def call(self, inputs: Any, state: Any): ...
