# Stubs for tensorflow.python.ops.collective_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import device as device
from tensorflow.python.ops import gen_collective_ops as gen_collective_ops
from typing import Any as Any

def all_reduce(t: Any, group_size: Any, group_key: Any, instance_key: Any, merge_op: Any, final_op: Any, subdiv_offsets: Any = ...): ...
def broadcast_send(t: Any, shape: Any, dtype: Any, group_size: Any, group_key: Any, instance_key: Any): ...
def broadcast_recv(shape: Any, dtype: Any, group_size: Any, group_key: Any, instance_key: Any): ...
