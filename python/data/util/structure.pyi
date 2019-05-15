# Stubs for tensorflow.python.data.util.structure (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import sparse_ops as sparse_ops
from typing import Any as Any

class Structure(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    @abc.abstractmethod
    def is_compatible_with(self, other: Any) -> Any: ...
    @staticmethod
    def from_value(value: Any): ...

class NestedStructure(Structure):
    def __init__(self, nested_structure: Any) -> None: ...
    def is_compatible_with(self, other: Any): ...
    @staticmethod
    def from_value(value: Any): ...

class TensorStructure(Structure):
    def __init__(self, dtype: Any, shape: Any) -> None: ...
    def is_compatible_with(self, other: Any): ...
    @staticmethod
    def from_value(value: Any): ...

class SparseTensorStructure(Structure):
    def __init__(self, dtype: Any, dense_shape: Any) -> None: ...
    def is_compatible_with(self, other: Any): ...
    @staticmethod
    def from_value(value: Any): ...