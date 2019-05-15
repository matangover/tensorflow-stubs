# Stubs for tensorflow.python.framework.op_def_library (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, op_def_pb2 as op_def_pb2, tensor_pb2 as tensor_pb2, tensor_shape_pb2 as tensor_shape_pb2, types_pb2 as types_pb2
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.util import compat as compat, tf_contextlib as tf_contextlib
from typing import Any as Any, Optional as Optional

class _OpInfo:
    op_def: Any = ...
    def __init__(self, op_def: Any) -> None: ...

class OpDefLibrary:
    def __init__(self) -> None: ...
    def add_op(self, op_def: Any) -> None: ...
    def add_op_list(self, op_list: Any) -> None: ...
    def apply_op(self, op_type_name: Any, name: Optional[Any] = ..., **keywords: Any): ...
