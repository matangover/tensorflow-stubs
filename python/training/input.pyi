# Stubs for tensorflow.python.training.input (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.layers import utils as utils
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, io_ops as io_ops, math_ops as math_ops, random_ops as random_ops, sparse_ops as sparse_ops
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import queue_runner as queue_runner
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def match_filenames_once(pattern: Any, name: Optional[Any] = ...): ...
def limit_epochs(tensor: Any, num_epochs: Optional[Any] = ..., name: Optional[Any] = ...): ...
def input_producer(input_tensor: Any, element_shape: Optional[Any] = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., seed: Optional[Any] = ..., capacity: int = ..., shared_name: Optional[Any] = ..., summary_name: Optional[Any] = ..., name: Optional[Any] = ..., cancel_op: Optional[Any] = ...): ...
def string_input_producer(string_tensor: Any, num_epochs: Optional[Any] = ..., shuffle: bool = ..., seed: Optional[Any] = ..., capacity: int = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ..., cancel_op: Optional[Any] = ...): ...
def range_input_producer(limit: Any, num_epochs: Optional[Any] = ..., shuffle: bool = ..., seed: Optional[Any] = ..., capacity: int = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def slice_input_producer(tensor_list: Any, num_epochs: Optional[Any] = ..., shuffle: bool = ..., seed: Optional[Any] = ..., capacity: int = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...

class _SparseMetaData:
    def __init__(self, sparse: Any, map_op: Any, rank: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def merge_with(self, other: Any): ...
    @property
    def map_op(self): ...
    @property
    def sparse(self): ...
    @property
    def rank(self): ...

def batch(tensors: Any, batch_size: Any, num_threads: int = ..., capacity: int = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., dynamic_pad: bool = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def maybe_batch(tensors: Any, keep_input: Any, batch_size: Any, num_threads: int = ..., capacity: int = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., dynamic_pad: bool = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def batch_join(tensors_list: Any, batch_size: Any, capacity: int = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., dynamic_pad: bool = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def maybe_batch_join(tensors_list: Any, keep_input: Any, batch_size: Any, capacity: int = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., dynamic_pad: bool = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def shuffle_batch(tensors: Any, batch_size: Any, capacity: Any, min_after_dequeue: Any, num_threads: int = ..., seed: Optional[Any] = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def maybe_shuffle_batch(tensors: Any, batch_size: Any, capacity: Any, min_after_dequeue: Any, keep_input: Any, num_threads: int = ..., seed: Optional[Any] = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def shuffle_batch_join(tensors_list: Any, batch_size: Any, capacity: Any, min_after_dequeue: Any, seed: Optional[Any] = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def maybe_shuffle_batch_join(tensors_list: Any, batch_size: Any, capacity: Any, min_after_dequeue: Any, keep_input: Any, seed: Optional[Any] = ..., enqueue_many: bool = ..., shapes: Optional[Any] = ..., allow_smaller_final_batch: bool = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
