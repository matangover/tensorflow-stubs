# Stubs for tensorflow.python.framework.tensor_shape (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import tensor_shape_pb2 as tensor_shape_pb2
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class Dimension:
    def __init__(self, value: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __int__(self): ...
    def __long__(self): ...
    def __index__(self): ...
    @property
    def value(self): ...
    def is_compatible_with(self, other: Any): ...
    def assert_is_compatible_with(self, other: Any) -> None: ...
    def merge_with(self, other: Any): ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __rsub__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __floordiv__(self, other: Any): ...
    def __rfloordiv__(self, other: Any): ...
    def __div__(self, other: Any): ...
    def __mod__(self, other: Any): ...
    def __rmod__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def __reduce__(self): ...

def as_dimension(value: Any): ...

class TensorShape:
    def __init__(self, dims: Any) -> None: ...
    @property
    def dims(self): ...
    @dims.setter
    def dims(self, dims: Any) -> None: ...
    @property
    def ndims(self): ...
    def __len__(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __iter__(self): ...
    def __getitem__(self, key: Any): ...
    def num_elements(self): ...
    def merge_with(self, other: Any): ...
    def concatenate(self, other: Any): ...
    def assert_same_rank(self, other: Any) -> None: ...
    def assert_has_rank(self, rank: Any) -> None: ...
    def with_rank(self, rank: Any): ...
    def with_rank_at_least(self, rank: Any): ...
    def with_rank_at_most(self, rank: Any): ...
    def is_compatible_with(self, other: Any): ...
    def assert_is_compatible_with(self, other: Any) -> None: ...
    def most_specific_compatible_shape(self, other: Any): ...
    def is_fully_defined(self): ...
    def assert_is_fully_defined(self) -> None: ...
    def as_list(self): ...
    def as_proto(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __reduce__(self): ...

def as_shape(shape: Any): ...
def unknown_shape(ndims: Optional[Any] = ...): ...
def scalar(): ...
def vector(length: Any): ...
def matrix(rows: Any, cols: Any): ...
