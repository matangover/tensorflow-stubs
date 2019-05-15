# Stubs for tensorflow.python.debug.lib.debug_gradients (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.debug.lib import debug_data as debug_data, debug_graphs as debug_graphs
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import gen_array_ops as gen_array_ops, variables as variables
from typing import Any as Any, Optional as Optional

class GradientsDebugger:
    def __init__(self, y_tensor: Optional[Any] = ...) -> None: ...
    @property
    def y_tensor(self): ...
    @property
    def graph(self): ...
    def __enter__(self) -> None: ...
    def __exit__(self, unused_type: Any, unused_value: Any, unused_traceback: Any) -> None: ...
    def identify_gradient(self, input_tensor: Any): ...
    def watch_gradients_by_tensors(self, graph: Any, tensors: Any): ...
    def watch_gradients_by_tensor_names(self, graph: Any, tensor_name_regex: Any): ...
    def register_gradient_tensor(self, x_tensor_name: Any, gradient_tensor: Any) -> None: ...
    def gradient_tensor(self, x_tensor: Any): ...
    def gradient_tensors(self): ...

def clear_gradient_debuggers() -> None: ...
def gradient_values_from_dump(grad_debugger: Any, x_tensor: Any, dump: Any): ...
