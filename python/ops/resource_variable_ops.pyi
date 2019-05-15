# Stubs for tensorflow.python.ops.resource_variable_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops.gen_resource_variable_ops import *
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, variable_pb2 as variable_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.eager import context as context, tape as tape
from tensorflow.python.framework import cpp_shape_inference_pb2 as cpp_shape_inference_pb2, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, gen_resource_variable_ops as gen_resource_variable_ops, gen_state_ops as gen_state_ops, math_ops as math_ops, variables as variables
from tensorflow.python.util import compat as compat
from typing import Any as Any, Optional as Optional

def get_resource_handle_data(graph_op: Any): ...
def eager_safe_variable_handle(shape: Any, dtype: Any, shared_name: Any, name: Any, graph_mode: Any): ...

class EagerResourceDeleter:
    def __init__(self, handle: Any, handle_device: Any) -> None: ...
    def __del__(self) -> None: ...

def shape_safe_assign_variable_handle(handle: Any, shape: Any, value: Any, name: Optional[Any] = ...): ...

class ResourceVariable(variables.RefVariable):
    def __init__(self, initial_value: Optional[Any] = ..., trainable: bool = ..., collections: Optional[Any] = ..., validate_shape: bool = ..., caching_device: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., variable_def: Optional[Any] = ..., import_scope: Optional[Any] = ..., constraint: Optional[Any] = ...) -> None: ...
    def __nonzero__(self): ...
    def __bool__(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    @property
    def dtype(self): ...
    @property
    def device(self): ...
    @property
    def graph(self): ...
    @property
    def name(self): ...
    @property
    def shape(self): ...
    @property
    def create(self): ...
    @property
    def handle(self): ...
    def value(self): ...
    @property
    def initializer(self): ...
    @property
    def initial_value(self): ...
    @property
    def constraint(self): ...
    @property
    def op(self): ...
    def eval(self, session: Optional[Any] = ...): ...
    def numpy(self): ...
    def count_up_to(self, limit: Any): ...
    def read_value(self): ...
    def sparse_read(self, indices: Any, name: Optional[Any] = ...): ...
    def to_proto(self, export_scope: Optional[Any] = ...): ...
    @staticmethod
    def from_proto(variable_def: Any, import_scope: Optional[Any] = ...): ...
    def set_shape(self, shape: Any) -> None: ...
    __array_priority__: int = ...
    def is_initialized(self, name: Optional[Any] = ...): ...
    def assign_sub(self, delta: Any, use_locking: Optional[Any] = ..., name: Optional[Any] = ..., read_value: bool = ...): ...
    def assign_add(self, delta: Any, use_locking: Optional[Any] = ..., name: Optional[Any] = ..., read_value: bool = ...): ...
    def assign(self, value: Any, use_locking: Optional[Any] = ..., name: Optional[Any] = ..., read_value: bool = ...): ...
    def __reduce__(self): ...
    def scatter_sub(self, sparse_delta: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
    def scatter_add(self, sparse_delta: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
    def scatter_update(self, sparse_delta: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
    def scatter_nd_sub(self, indices: Any, updates: Any, name: Optional[Any] = ...): ...
    def scatter_nd_add(self, indices: Any, updates: Any, name: Optional[Any] = ...): ...
    def scatter_nd_update(self, indices: Any, updates: Any, name: Optional[Any] = ...): ...
    def __int__(self): ...
    def __iadd__(self, unused_other: Any) -> None: ...
    def __isub__(self, unused_other: Any) -> None: ...
    def __imul__(self, unused_other: Any) -> None: ...
    def __idiv__(self, unused_other: Any) -> None: ...
    def __itruediv__(self, unused_other: Any) -> None: ...
    def __irealdiv__(self, unused_other: Any) -> None: ...
    def __ipow__(self, unused_other: Any) -> None: ...

class _UnreadVariable(ResourceVariable):
    def __init__(self, handle: Any, dtype: Any, shape: Any, in_graph_mode: Any, deleter: Any, parent_op: Any, unique_id: Any) -> None: ...
    @property
    def name(self): ...
    def value(self): ...
    def read_value(self): ...
    def set_shape(self, shape: Any) -> None: ...
    @property
    def op(self): ...

class _MixedPrecisionVariable(ResourceVariable):
    def __init__(self, var: Any, read_dtype: Any) -> None: ...
    @property
    def name(self): ...
    def value(self): ...
    def read_value(self): ...
    def set_shape(self, shape: Any) -> None: ...
    @property
    def op(self): ...
    @property
    def read_dtype(self): ...

def is_resource_variable(var: Any): ...