# Stubs for tensorflow.python.ops.gen_control_flow_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def abort(error_msg: str = ..., exit_without_error: bool = ..., name: Optional[Any] = ...): ...
def abort_eager_fallback(error_msg: str = ..., exit_without_error: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def control_trigger(name: Optional[Any] = ...): ...
def control_trigger_eager_fallback(name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def enter(data: Any, frame_name: Any, is_constant: bool = ..., parallel_iterations: int = ..., name: Optional[Any] = ...): ...
def enter_eager_fallback(data: Any, frame_name: Any, is_constant: bool = ..., parallel_iterations: int = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def loop_cond(input: Any, name: Optional[Any] = ...): ...
def loop_cond_eager_fallback(input: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _MergeOutput = namedtuple('Merge', <ERROR>)

def merge(inputs: Any, name: Optional[Any] = ...): ...
def merge_eager_fallback(inputs: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def next_iteration(data: Any, name: Optional[Any] = ...): ...
def next_iteration_eager_fallback(data: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def no_op(name: Optional[Any] = ...): ...
def no_op_eager_fallback(name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def ref_enter(data: Any, frame_name: Any, is_constant: bool = ..., parallel_iterations: int = ..., name: Optional[Any] = ...): ...
def ref_exit(data: Any, name: Optional[Any] = ...): ...

# _RefMergeOutput = namedtuple('RefMerge', <ERROR>)

def ref_merge(inputs: Any, name: Optional[Any] = ...): ...
def ref_next_iteration(data: Any, name: Optional[Any] = ...): ...
def ref_select(index: Any, inputs: Any, name: Optional[Any] = ...): ...

# _RefSwitchOutput = namedtuple('RefSwitch', <ERROR>)

def ref_switch(data: Any, pred: Any, name: Optional[Any] = ...): ...

# _SwitchOutput = namedtuple('Switch', <ERROR>)

def switch(data: Any, pred: Any, name: Optional[Any] = ...): ...
def switch_eager_fallback(data: Any, pred: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...