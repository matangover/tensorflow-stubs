# Stubs for tensorflow.python.framework.constant_op (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, types_pb2 as types_pb2
from tensorflow.python.eager import context as context, execute as execute
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def convert_to_eager_tensor(value: Any, ctx: Any, dtype: Optional[Any] = ...): ...
def constant(value: Any, dtype: Optional[Any] = ..., shape: Optional[Any] = ..., name: str = ..., verify_shape: bool = ...): ...
def is_constant(tensor_or_op: Any): ...