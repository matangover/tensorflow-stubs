# Stubs for tensorflow.python.ops.gen_collective_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def collective_bcast_recv(T: Any, group_size: Any, group_key: Any, instance_key: Any, shape: Any, name: Optional[Any] = ...): ...
def collective_bcast_recv_eager_fallback(T: Any, group_size: Any, group_key: Any, instance_key: Any, shape: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def collective_bcast_send(input: Any, group_size: Any, group_key: Any, instance_key: Any, shape: Any, name: Optional[Any] = ...): ...
def collective_bcast_send_eager_fallback(input: Any, group_size: Any, group_key: Any, instance_key: Any, shape: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def collective_reduce(input: Any, group_size: Any, group_key: Any, instance_key: Any, merge_op: Any, final_op: Any, subdiv_offsets: Any, name: Optional[Any] = ...): ...
def collective_reduce_eager_fallback(input: Any, group_size: Any, group_key: Any, instance_key: Any, merge_op: Any, final_op: Any, subdiv_offsets: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
