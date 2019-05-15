# Stubs for tensorflow.python.ops.sets_impl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import gen_set_ops as gen_set_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

def set_size(a: Any, validate_indices: bool = ...): ...
def set_intersection(a: Any, b: Any, validate_indices: bool = ...): ...
def set_difference(a: Any, b: Any, aminusb: bool = ..., validate_indices: bool = ...): ...
def set_union(a: Any, b: Any, validate_indices: bool = ...): ...