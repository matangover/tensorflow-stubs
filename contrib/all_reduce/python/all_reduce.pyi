# Stubs for tensorflow.contrib.all_reduce.python.all_reduce (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib import nccl as nccl
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

def build_ring_all_reduce(input_tensors: Any, num_workers: Any, num_subchunks: Any, gpu_perm: Any, red_op: Any, un_op: Optional[Any] = ...): ...
def build_recursive_hd_all_reduce(input_tensors: Any, red_op: Any, un_op: Optional[Any] = ...): ...
def build_shuffle_all_reduce(input_tensors: Any, gather_devices: Any, red_op: Any, un_op: Optional[Any] = ...): ...
def build_nccl_all_reduce(input_tensors: Any, red_op: Any, un_op: Optional[Any] = ...): ...
def build_nccl_then_ring(input_tensors: Any, subdiv: Any, red_op: Any, un_op: Optional[Any] = ...): ...
def build_nccl_then_recursive_hd(input_tensors: Any, red_op: Any, un_op: Optional[Any] = ...): ...
def build_nccl_then_shuffle(input_tensors: Any, gather_devices: Any, nccl_red_op: Any, shuffle_red_op: Any, un_op: Optional[Any] = ...): ...
def build_shuffle_then_ring(input_tensors: Any, gather_devices: Any, subdiv: Any, red_n_op: Any, red_op: Any, un_op: Optional[Any] = ...): ...
def build_shuffle_then_shuffle(input_tensors: Any, first_gather_devices: Any, second_gather_devices: Any, red_op: Any, un_op: Optional[Any] = ...): ...