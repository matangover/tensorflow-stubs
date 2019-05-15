# Stubs for tensorflow.python.ops.parsing_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops.gen_parsing_ops import *
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_parsing_ops as gen_parsing_ops, math_ops as math_ops, sparse_ops as sparse_ops
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class VarLenFeature: ...

class SparseFeature:
    def __new__(cls, index_key: Any, value_key: Any, dtype: Any, size: Any, already_sorted: bool = ...): ...

class FixedLenFeature:
    def __new__(cls, shape: Any, dtype: Any, default_value: Optional[Any] = ...): ...

class FixedLenSequenceFeature:
    def __new__(cls, shape: Any, dtype: Any, allow_missing: bool = ..., default_value: Optional[Any] = ...): ...

def parse_example(serialized: Any, features: Any, name: Optional[Any] = ..., example_names: Optional[Any] = ...): ...
def parse_single_example(serialized: Any, features: Any, name: Optional[Any] = ..., example_names: Optional[Any] = ...): ...
def parse_sequence_example(serialized: Any, context_features: Optional[Any] = ..., sequence_features: Optional[Any] = ..., example_names: Optional[Any] = ..., name: Optional[Any] = ...): ...
def parse_single_sequence_example(serialized: Any, context_features: Optional[Any] = ..., sequence_features: Optional[Any] = ..., example_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def decode_csv(records: Any, record_defaults: Any, field_delim: str = ..., use_quote_delim: bool = ..., name: Optional[Any] = ..., na_value: str = ..., select_cols: Optional[Any] = ...): ...
def parse_single_example_v2(serialized: Any, features: Any, name: Optional[Any] = ...): ...
