# Stubs for tensorflow.contrib.distribute.python.prefetching_ops_v2 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.experimental.ops import prefetching_ops as prefetching_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.data.util import sparse as sparse
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, function as function, ops as ops
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

class _PrefetchToDeviceIterator:
    def __init__(self, input_dataset: Any, one_shot: Any, devices: Any, buffer_size: Any, shared_name: Optional[Any] = ...) -> None: ...
    def get_next(self, name: Optional[Any] = ...): ...
    @property
    def initializer(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class _PrefetchToDeviceDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, devices: Any, buffer_size: Any) -> None: ...
    def make_one_shot_iterator(self): ...
    def make_initializable_iterator(self, shared_name: Optional[Any] = ...): ...
    @property
    def output_types(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_classes(self): ...

def prefetch_to_devices(devices: Any, buffer_size: Optional[Any] = ...): ...
