# Stubs for tensorflow.contrib.rnn.python.ops.rnn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops import array_ops as array_ops, rnn as rnn
from typing import Any as Any, Optional as Optional

def stack_bidirectional_rnn(cells_fw: Any, cells_bw: Any, inputs: Any, initial_states_fw: Optional[Any] = ..., initial_states_bw: Optional[Any] = ..., dtype: Optional[Any] = ..., sequence_length: Optional[Any] = ..., scope: Optional[Any] = ...): ...
def stack_bidirectional_dynamic_rnn(cells_fw: Any, cells_bw: Any, inputs: Any, initial_states_fw: Optional[Any] = ..., initial_states_bw: Optional[Any] = ..., dtype: Optional[Any] = ..., sequence_length: Optional[Any] = ..., parallel_iterations: Optional[Any] = ..., time_major: bool = ..., scope: Optional[Any] = ...): ...