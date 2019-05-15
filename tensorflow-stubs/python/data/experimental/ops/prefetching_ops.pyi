# Stubs for tensorflow.python.data.experimental.ops.prefetching_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.data.util import nest as nest, sparse as sparse
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, function as function, ops as ops
from tensorflow.python.ops import array_ops as array_ops, functional_ops as functional_ops, gen_dataset_ops as gen_dataset_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def function_buffering_resource(string_arg: Any, target_device: Any, f: Any, buffer_size: Any, output_types: Any, container: str = ..., shared_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def function_buffering_resource_get_next(function_buffer_resource: Any, output_types: Any, name: Optional[Any] = ...): ...
def function_buffering_resource_reset(function_buffer_resource: Any, name: Optional[Any] = ...): ...

class _PrefetchToDeviceIterator:
    def __init__(self, input_dataset: Any, one_shot: Any, device: Any, buffer_size: Any, shared_name: Optional[Any] = ...) -> None: ...
    def get_next(self, name: Optional[Any] = ...): ...
    @property
    def initializer(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class _PrefetchToDeviceEagerIterator(iterator_ops.EagerIterator):
    def __init__(self, input_dataset: Any, device: Any, buffer_size: Any) -> None: ...

class _PrefetchToDeviceDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, device: Any, buffer_size: Any) -> None: ...
    def __iter__(self): ...
    def make_one_shot_iterator(self): ...
    def make_initializable_iterator(self, shared_name: Optional[Any] = ...): ...
    @property
    def output_types(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_classes(self): ...

def prefetch_to_device(device: Any, buffer_size: Optional[Any] = ...): ...
def copy_to_device(target_device: Any, source_device: str = ...): ...

class _CopyToDeviceDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, target_device: Any, source_device: str = ...) -> None: ...
    def make_one_shot_iterator(self): ...
    @property
    def output_types(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_classes(self): ...