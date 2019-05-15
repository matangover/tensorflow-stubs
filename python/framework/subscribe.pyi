# Stubs for tensorflow.python.framework.subscribe (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, variables as variables
from typing import Any as Any

class _ControlOutputCache:
    cache: Any = ...
    def __init__(self) -> None: ...
    def calc_control_outputs(self, graph: Any): ...
    def get_control_outputs(self, op: Any): ...

def subscribe(tensors: Any, side_effects: Any): ...
