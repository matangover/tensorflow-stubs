# Stubs for tensorflow.contrib.layers.python.layers.rev_block_lib (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import backprop as backprop
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.layers import base as base
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, custom_gradient as custom_gradient, gradients_impl as gradients_impl, math_ops as math_ops, variable_scope as variable_scope
from tensorflow.python.util import nest as nest, tf_inspect as tf_inspect
from typing import Any as Any, Optional as Optional

class RevBlock(base.Layer):
    f: Any = ...
    g: Any = ...
    num_layers: Any = ...
    f_side_input: Any = ...
    g_side_input: Any = ...
    def __init__(self, f: Any, g: Any, num_layers: int = ..., f_side_input: Optional[Any] = ..., g_side_input: Optional[Any] = ..., use_efficient_backprop: bool = ..., name: str = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, forward: bool = ...): ...
    def forward(self, x1: Any, x2: Any): ...
    def backward(self, y1: Any, y2: Any): ...
    built: bool = ...
    def build(self, _: Any) -> None: ...

def rev_block(x1: Any, x2: Any, f: Any, g: Any, num_layers: int = ..., f_side_input: Optional[Any] = ..., g_side_input: Optional[Any] = ..., is_training: bool = ...): ...
def recompute_grad(fn: Any, use_data_dep: Any = ..., tupleize_grads: bool = ...): ...