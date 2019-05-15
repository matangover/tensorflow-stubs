# Stubs for tensorflow.python.ops.gen_state_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def assign(ref: Any, value: Any, validate_shape: bool = ..., use_locking: bool = ..., name: Optional[Any] = ...): ...
def assign_add(ref: Any, value: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def assign_sub(ref: Any, value: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def count_up_to(ref: Any, limit: Any, name: Optional[Any] = ...): ...
def destroy_temporary_variable(ref: Any, var_name: Any, name: Optional[Any] = ...): ...
def is_variable_initialized(ref: Any, name: Optional[Any] = ...): ...
def resource_count_up_to(resource: Any, limit: Any, T: Any, name: Optional[Any] = ...): ...
def resource_count_up_to_eager_fallback(resource: Any, limit: Any, T: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_scatter_nd_add(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_scatter_nd_add_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_scatter_nd_update(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_scatter_nd_update_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def scatter_add(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_div(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_max(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_min(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_mul(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_nd_add(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_nd_sub(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_nd_update(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_sub(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def scatter_update(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def temporary_variable(shape: Any, dtype: Any, var_name: str = ..., name: Optional[Any] = ...): ...
def variable(shape: Any, dtype: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...
def variable_v2(shape: Any, dtype: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...