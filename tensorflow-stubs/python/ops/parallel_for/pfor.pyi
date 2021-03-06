# Stubs for tensorflow.python.ops.parallel_for.pfor (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, bitwise_ops as bitwise_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, functional_ops as functional_ops, gen_parsing_ops as gen_parsing_ops, gen_sparse_ops as gen_sparse_ops, math_ops as math_ops, nn_ops as nn_ops, parsing_ops as parsing_ops, sparse_ops as sparse_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.platform import flags as flags
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

passthrough_stateful_ops: Any

class WhileOp:
    def __init__(self, exit_node: Any, pfor_ops: Any) -> None: ...
    @property
    def inputs(self): ...
    @property
    def control_inputs(self): ...
    @property
    def outputs(self): ...
    @property
    def name(self): ...
    @property
    def is_inside_loop(self): ...
    def op_is_inside_loop(self, op: Any): ...
    @property
    def is_stateful(self): ...
    @property
    def pfor_converter(self): ...
    def __call__(self, pfor_input: Any): ...

class _PforInput:
    pfor: Any = ...
    def __init__(self, pfor: Any, op: Any, inputs: Any) -> None: ...
    def stack_inputs(self, stack_indices: Optional[Any] = ...) -> None: ...
    def expanddim_inputs_for_broadcast(self): ...
    @property
    def inputs(self): ...
    @property
    def num_inputs(self): ...
    def input(self, index: Any): ...
    def stacked_input(self, index: Any): ...
    def unstacked_input(self, index: Any): ...
    @property
    def op(self): ...
    @property
    def op_type(self): ...
    def get_attr(self, attr: Any): ...
    @property
    def outputs(self): ...
    def output(self, index: Any): ...

class RegisterPFor:
    op_type: Any = ...
    def __init__(self, op_type: Any) -> None: ...
    def __call__(self, converter: Any): ...

class RegisterPForWithArgs(RegisterPFor):
    def __init__(self, op_type: Any, *args: Any, **kw_args: Any) -> None: ...
    def __call__(self, converter: Any): ...

WrappedTensor = namedtuple('WrappedTensor', ['t', 'is_stacked', 'is_sparse_stacked'])

def wrap(tensor: Any, is_stacked: bool = ..., is_sparse_stacked: bool = ...): ...

class PFor:
    all_indices: Any = ...
    def __init__(self, loop_var: Any, loop_len: Any, pfor_ops: Any, all_indices: Optional[Any] = ..., all_indices_partitioned: bool = ...) -> None: ...
    def op_is_inside_loop(self, op: Any): ...
    def convert(self, y: Any): ...
    @property
    def loop_len_vector(self): ...
    @property
    def loop_var(self): ...
    @property
    def pfor_ops(self): ...
    @property
    def all_indices_partitioned(self): ...
