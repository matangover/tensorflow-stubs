# Stubs for tensorflow.python.data.ops.multi_device_iterator_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest, sparse as sparse
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, function as function, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, functional_ops as functional_ops, gen_dataset_ops as gen_dataset_ops
from typing import Any as Any

class _PerDeviceGenerator(dataset_ops.Dataset):
    def __init__(self, shard_num: Any, multi_device_iterator_resource: Any, incarnation_id: Any, source_device: Any, target_device: Any, output_shapes: Any, output_types: Any, output_classes: Any) -> None: ...
    @property
    def output_types(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_classes(self): ...

class MultiDeviceIterator:
    def __init__(self, dataset: Any, devices: Any, max_buffer_size: int = ..., prefetch_buffer_size: int = ..., source_device: str = ...) -> None: ...
    def get_next(self): ...
    @property
    def initializer(self): ...
