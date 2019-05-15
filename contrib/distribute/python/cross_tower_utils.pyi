# Stubs for tensorflow.contrib.distribute.python.cross_tower_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.contrib import nccl as nccl
from tensorflow.contrib.all_reduce.python import all_reduce as all_reduce
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, collective_ops as collective_ops, gradients_impl as gradients_impl, math_ops as math_ops
from typing import Any as Any, Optional as Optional

def aggregate_gradients_using_nccl(tower_grads: Any): ...
def aggregate_gradients_using_hierarchical_copy(avail_devices: Any, tower_grads: Any): ...
def aggregate_single_gradient_using_copy(grad_and_vars: Any, use_mean: Any, check_inf_nan: Any): ...
def group_device_names(devices: Any, group_size: Any): ...
def split_grads_by_size(threshold_size: Any, device_grads: Any): ...

class CollectiveKeys:
    def __init__(self, group_key_start: int = ..., instance_key_start: int = ..., instance_key_with_id_start: int = ...) -> None: ...
    def get_group_key(self, devices: Any): ...
    def get_instance_key(self, key_id: Optional[Any] = ...): ...

def build_collective_reduce(input_tensors: Any, num_workers: Any, collective_keys: Any, reduction_op: str = ..., unary_op: str = ...): ...
def sum_grad_and_var_all_reduce(grad_and_vars: Any, num_workers: Any, alg: Any, gpu_indices: Any, aux_devices: Optional[Any] = ..., num_shards: int = ...): ...
def sum_gradients_all_reduce(dev_prefixes: Any, tower_grads: Any, num_workers: Any, alg: Any, num_shards: Any, gpu_indices: Any): ...
def extract_ranges(index_list: Any, range_size_limit: int = ...): ...

GradPackTuple = namedtuple('GradPackTuple', 'indices vars shapes')

def pack_range(key: Any, packing: Any, grad_vars: Any, rng: Any): ...
def unpack_grad_tuple(gv: Any, gpt: Any): ...
def pack_small_tensors(tower_grads: Any, max_bytes: int = ..., max_group: int = ...): ...
def unpack_small_tensors(tower_grads: Any, packing: Any): ...
def aggregate_tensors_or_indexed_slices(values: Any, accumulation_fn: Any = ...): ...
def divide_by_n_tensors_or_indexed_slices(value: Any, n: Any): ...
def copy_tensor_or_indexed_slices_to_device(value: Any, device: Any): ...
def contains_indexed_slices(value: Any): ...
