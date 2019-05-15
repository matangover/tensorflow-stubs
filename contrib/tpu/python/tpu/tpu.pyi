# Stubs for tensorflow.contrib.tpu.python.tpu.tpu (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.contrib.framework.python.framework import experimental as experimental
from tensorflow.contrib.tpu.python.ops import tpu_ops as tpu_ops
from tensorflow.contrib.tpu.python.tpu import tpu_function as tpu_function
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, variable_scope as variable_scope
from tensorflow.python.util import compat as compat
from typing import Any as Any, Optional as Optional

def initialize_system(embedding_config: Optional[Any] = ..., job: Optional[Any] = ...): ...
def shutdown_system(job: Optional[Any] = ...): ...
def core(num: Any): ...

class TPUReplicateContext(control_flow_ops.XLAControlFlowContext, metaclass=abc.ABCMeta):
    def __init__(self, name: Any, num_replicas: Any, pivot: Any) -> None: ...
    def get_replicated_var_handle(self, name: Any, vars_: Any): ...
    def report_unsupported_operations(self) -> None: ...
    def EnterGradientColocation(self, op: Any, gradient_uid: Any) -> None: ...
    def ExitGradientColocation(self, op: Any, gradient_uid: Any) -> None: ...
    def Enter(self) -> None: ...
    def HostComputeCore(self): ...
    def AddOp(self, op: Any) -> None: ...
    def AddValue(self, val: Any): ...
    def AddInnerOp(self, op: Any) -> None: ...
    @property
    def grad_state(self) -> None: ...
    @property
    def back_prop(self): ...
    def GetControlPivot(self): ...

def outside_compilation(computation: Any, *args: Any, **kwargs: Any): ...
def replicate(computation: Any, inputs: Optional[Any] = ..., infeed_queue: Optional[Any] = ..., device_assignment: Optional[Any] = ..., name: Optional[Any] = ...): ...
def split_compile_and_replicate(computation: Any, inputs: Optional[Any] = ..., infeed_queue: Optional[Any] = ..., device_assignment: Optional[Any] = ..., name: Optional[Any] = ..., use_tpu: bool = ...): ...
def shard(computation: Any, inputs: Optional[Any] = ..., num_shards: int = ..., input_shard_axes: Optional[Any] = ..., outputs_from_all_shards: bool = ..., output_shard_axes: Optional[Any] = ..., infeed_queue: Optional[Any] = ..., device_assignment: Optional[Any] = ..., name: Optional[Any] = ...): ...
def batch_parallel(computation: Any, inputs: Optional[Any] = ..., num_shards: int = ..., infeed_queue: Optional[Any] = ..., device_assignment: Optional[Any] = ..., name: Optional[Any] = ...): ...
def rewrite(computation: Any, inputs: Optional[Any] = ..., infeed_queue: Optional[Any] = ..., device_assignment: Optional[Any] = ..., name: Optional[Any] = ...): ...
def under_tpu_inference_context(): ...

class _TPUInferenceContext(control_flow_ops.XLAControlFlowContext, metaclass=abc.ABCMeta):
    def __init__(self, name: Any) -> None: ...
    def AddOp(self, op: Any) -> None: ...
    def AddValue(self, val: Any): ...
    def AddInnerOp(self, op: Any) -> None: ...
    @property
    def grad_state(self) -> None: ...

def validate_inference_rewrite_for_variables(graph: Any) -> None: ...
def rewrite_for_inference(computation: Any, inputs: Optional[Any] = ..., infeed_queue: Optional[Any] = ..., device_assignment: Optional[Any] = ..., name: Optional[Any] = ...): ...
