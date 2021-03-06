# Stubs for tensorflow.contrib.layers.python.layers.normalization (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.framework.python.ops import add_arg_scope as add_arg_scope, variables as variables
from tensorflow.contrib.layers.python.layers import utils as utils
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, math_ops as math_ops, nn as nn, variable_scope as variable_scope
from typing import Any as Any, Optional as Optional

def instance_norm(inputs: Any, center: bool = ..., scale: bool = ..., epsilon: float = ..., activation_fn: Optional[Any] = ..., param_initializers: Optional[Any] = ..., reuse: Optional[Any] = ..., variables_collections: Optional[Any] = ..., outputs_collections: Optional[Any] = ..., trainable: bool = ..., data_format: Any = ..., scope: Optional[Any] = ...): ...
def group_norm(inputs: Any, groups: int = ..., channels_axis: int = ..., reduction_axes: Any = ..., center: bool = ..., scale: bool = ..., epsilon: float = ..., activation_fn: Optional[Any] = ..., param_initializers: Optional[Any] = ..., reuse: Optional[Any] = ..., variables_collections: Optional[Any] = ..., outputs_collections: Optional[Any] = ..., trainable: bool = ..., scope: Optional[Any] = ..., mean_close_to_zero: bool = ...): ...
