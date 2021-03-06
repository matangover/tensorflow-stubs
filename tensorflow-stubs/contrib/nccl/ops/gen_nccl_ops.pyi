# Stubs for tensorflow.contrib.nccl.ops.gen_nccl_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def nccl_all_reduce(input: Any, reduction: Any, num_devices: Any, shared_name: Any, name: Optional[Any] = ...): ...
def nccl_all_reduce_eager_fallback(input: Any, reduction: Any, num_devices: Any, shared_name: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def nccl_broadcast(input: Any, shape: Any, name: Optional[Any] = ...): ...
def nccl_broadcast_eager_fallback(input: Any, shape: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def nccl_reduce(input: Any, reduction: Any, name: Optional[Any] = ...): ...
def nccl_reduce_eager_fallback(input: Any, reduction: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
