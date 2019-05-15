# Stubs for tensorflow.contrib.compiler.xla (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.compiler.jit.ops import xla_ops as xla_ops
from tensorflow.contrib.tpu.python.tpu import tpu_function as tpu_function
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, summary_op_util as summary_op_util, variable_scope as variable_scope
from tensorflow.python.util import compat as compat, function_utils as function_utils, tf_decorator as tf_decorator
from typing import Any as Any, Optional as Optional

def compile(computation: Any, inputs: Optional[Any] = ...): ...

class XLACompileContext(control_flow_ops.XLAControlFlowContext, metaclass=abc.ABCMeta):
    def __init__(self, name: Any, pivot: Any) -> None: ...
    def report_unsupported_operations(self) -> None: ...
    def AddOp(self, op: Any) -> None: ...
    def AddValue(self, val: Any): ...
    def AddInnerOp(self, op: Any) -> None: ...
    @property
    def grad_state(self) -> None: ...
    @property
    def back_prop(self): ...

class _CapturedObject:
    def __init__(self) -> None: ...
    def capture(self, o: Any) -> None: ...
    def get(self): ...

class _ModelFnWrapper:
    def __init__(self, function: Any) -> None: ...
    def __call__(self, features: Any, labels: Any, mode: Any, params: Any): ...

def estimator_model_fn(target_model_fn: Optional[Any] = ...): ...
