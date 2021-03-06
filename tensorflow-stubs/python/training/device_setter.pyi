# Stubs for tensorflow.python.training.device_setter (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import node_def_pb2 as node_def_pb2
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

STANDARD_PS_OPS: Any

class _RoundRobinStrategy:
    def __init__(self, num_tasks: Any) -> None: ...
    def __call__(self, unused_op: Any): ...

class _ReplicaDeviceChooser:
    def __init__(self, ps_tasks: Any, ps_device: Any, worker_device: Any, merge_devices: Any, ps_ops: Any, ps_strategy: Any) -> None: ...
    def device_function(self, op: Any): ...

def replica_device_setter(ps_tasks: int = ..., ps_device: str = ..., worker_device: str = ..., merge_devices: bool = ..., cluster: Optional[Any] = ..., ps_ops: Optional[Any] = ..., ps_strategy: Optional[Any] = ...): ...
