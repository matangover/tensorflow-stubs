# Stubs for tensorflow.contrib.grid_rnn.python.ops.grid_rnn_cell (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.contrib import layers as layers, rnn as rnn
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn
from typing import Any as Any, Optional as Optional

class GridRNNCell(rnn.RNNCell):
    def __init__(self, num_units: Any, num_dims: int = ..., input_dims: Optional[Any] = ..., output_dims: Optional[Any] = ..., priority_dims: Optional[Any] = ..., non_recurrent_dims: Optional[Any] = ..., tied: bool = ..., cell_fn: Optional[Any] = ..., non_recurrent_fn: Optional[Any] = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...
    @property
    def output_size(self): ...
    @property
    def state_size(self): ...
    def __call__(self, inputs: Any, state: Any, scope: Optional[Any] = ...): ...

class Grid1BasicRNNCell(GridRNNCell):
    def __init__(self, num_units: Any, state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

class Grid2BasicRNNCell(GridRNNCell):
    def __init__(self, num_units: Any, tied: bool = ..., non_recurrent_fn: Optional[Any] = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

class Grid1BasicLSTMCell(GridRNNCell):
    def __init__(self, num_units: Any, forget_bias: int = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

class Grid2BasicLSTMCell(GridRNNCell):
    def __init__(self, num_units: Any, tied: bool = ..., non_recurrent_fn: Optional[Any] = ..., forget_bias: int = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

class Grid1LSTMCell(GridRNNCell):
    def __init__(self, num_units: Any, use_peepholes: bool = ..., forget_bias: float = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

class Grid2LSTMCell(GridRNNCell):
    def __init__(self, num_units: Any, tied: bool = ..., non_recurrent_fn: Optional[Any] = ..., use_peepholes: bool = ..., forget_bias: float = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

class Grid3LSTMCell(GridRNNCell):
    def __init__(self, num_units: Any, tied: bool = ..., non_recurrent_fn: Optional[Any] = ..., use_peepholes: bool = ..., forget_bias: float = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

class Grid2GRUCell(GridRNNCell):
    def __init__(self, num_units: Any, tied: bool = ..., non_recurrent_fn: Optional[Any] = ..., state_is_tuple: bool = ..., output_is_tuple: bool = ...) -> None: ...

_GridRNNDimension = namedtuple('_GridRNNDimension', ['idx', 'is_input', 'is_output', 'is_priority', 'non_recurrent_fn'])

_GridRNNConfig = namedtuple('_GridRNNConfig', ['num_dims', 'dims', 'inputs', 'outputs', 'recurrents', 'priority', 'non_priority', 'tied', 'num_units'])
