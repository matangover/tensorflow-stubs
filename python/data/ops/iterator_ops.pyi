# Stubs for tensorflow.python.data.ops.iterator_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.compat import compat as compat
from tensorflow.python.data.ops import optional_ops as optional_ops
from tensorflow.python.data.util import nest as nest, sparse as sparse, structure as structure
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, errors as errors, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.training.checkpointable import base as checkpointable
from tensorflow.python.training.saver import BaseSaverBuilder as BaseSaverBuilder
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

GET_NEXT_CALL_WARNING_THRESHOLD: int
GET_NEXT_CALL_WARNING_MESSAGE: str
GLOBAL_ITERATORS: str

class Iterator(checkpointable.CheckpointableBase):
    def __init__(self, iterator_resource: Any, initializer: Any, output_types: Any, output_shapes: Any, output_classes: Any) -> None: ...
    @staticmethod
    def from_structure(output_types: Any, output_shapes: Optional[Any] = ..., shared_name: Optional[Any] = ..., output_classes: Optional[Any] = ...): ...
    @staticmethod
    def from_string_handle(string_handle: Any, output_types: Any, output_shapes: Optional[Any] = ..., output_classes: Optional[Any] = ...): ...
    @property
    def initializer(self): ...
    def make_initializer(self, dataset: Any, name: Optional[Any] = ...): ...
    def get_next(self, name: Optional[Any] = ...): ...
    def string_handle(self, name: Optional[Any] = ...): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class EagerIterator(checkpointable.CheckpointableBase):
    def __init__(self, dataset: Any) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def next(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    def get_next(self, name: Optional[Any] = ...): ...

class _IteratorSaveable(BaseSaverBuilder.SaveableObject):
    def __init__(self, iterator_resource: Any, name: Any) -> None: ...
    def restore(self, restored_tensors: Any, restored_shapes: Any): ...

def get_next_as_optional(iterator: Any): ...
