# Stubs for tensorflow.python.data.util.sparse (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import sparse_ops as sparse_ops
from typing import Any as Any

def any_sparse(classes: Any): ...
def as_dense_shapes(shapes: Any, classes: Any): ...
def as_dense_types(types: Any, classes: Any): ...
def deserialize_sparse_tensors(tensors: Any, types: Any, shapes: Any, classes: Any): ...
def get_classes(tensors: Any): ...
def serialize_many_sparse_tensors(tensors: Any): ...
def serialize_sparse_tensors(tensors: Any): ...
