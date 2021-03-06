# Stubs for tensorflow.contrib.quantize.python.quantize (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.quantize.python import common as common, graph_matcher as graph_matcher, input_to_ops as input_to_ops, quant_ops as quant_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

def Quantize(graph: Any, is_training: Any, weight_bits: int = ..., activation_bits: int = ..., ema_decay: float = ..., quant_delay: Optional[Any] = ..., vars_collection: Any = ..., scope: Optional[Any] = ...) -> None: ...

class _LayerMatch:
    def __init__(self, layer_op: Any, weight_tensor: Any, activation_op: Any, bypass_op: Any, post_activation_bypass_op: Any, bias_add_op: Any) -> None: ...
    @property
    def layer_op(self): ...
    @property
    def weight_tensor(self): ...
    @property
    def activation_op(self): ...
    @property
    def bypass_op(self): ...
    @property
    def post_activation_bypass_op(self): ...
    @property
    def bias_add_op(self): ...
