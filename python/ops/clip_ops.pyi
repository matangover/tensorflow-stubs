# Stubs for tensorflow.python.ops.clip_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, gen_nn_ops as gen_nn_ops, math_ops as math_ops, numerics as numerics
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def clip_by_value(t: Any, clip_value_min: Any, clip_value_max: Any, name: Optional[Any] = ...): ...
def clip_by_norm(t: Any, clip_norm: Any, axes: Optional[Any] = ..., name: Optional[Any] = ...): ...
def global_norm(t_list: Any, name: Optional[Any] = ...): ...
def clip_by_global_norm(t_list: Any, clip_norm: Any, use_norm: Optional[Any] = ..., name: Optional[Any] = ...): ...
def clip_by_average_norm(t: Any, clip_norm: Any, name: Optional[Any] = ...): ...
