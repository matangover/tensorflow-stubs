# Stubs for tensorflow.contrib.labeled_tensor.python.ops.sugar (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.labeled_tensor.python.ops import core as core, ops as ops
from typing import Any as Any, Optional as Optional

class ReshapeCoder:
    def __init__(self, existing_axis_names: Any, new_axes: Any, name: Optional[Any] = ...) -> None: ...
    def encode(self, labeled_tensor: Any): ...
    def decode(self, labeled_tensor: Any): ...
