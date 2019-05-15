# Stubs for tensorflow.python.debug.lib.stepper (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.debug.lib import debug_data as debug_data, debug_graphs as debug_graphs, debug_utils as debug_utils
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import session_ops as session_ops
from typing import Any as Any, Optional as Optional

class NodeStepper:
    FEED_TYPE_CLIENT: str = ...
    FEED_TYPE_HANDLE: str = ...
    FEED_TYPE_OVERRIDE: str = ...
    FEED_TYPE_DUMPED_INTERMEDIATE: str = ...
    def __init__(self, sess: Any, fetches: Any, feed_dict: Optional[Any] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, exc_traceback: Any) -> None: ...
    def sorted_nodes(self): ...
    def closure_elements(self): ...
    def output_slots_in_closure(self, node_name: Any): ...
    def is_feedable(self, name: Any): ...
    def override_tensor(self, tensor_name: Any, overriding_val: Any) -> None: ...
    def remove_override(self, tensor_name: Any) -> None: ...
    def last_feed_types(self): ...
    def cont(self, target: Any, use_tensor_handles: bool = ..., use_dumped_intermediates: bool = ..., use_overrides: bool = ..., invalidate_from_updated_variables: bool = ..., restore_variable_values: bool = ...): ...
    def finalize(self): ...
    def restore_variable_values(self) -> None: ...
    def handle_names(self): ...
    def handle_node_names(self): ...
    def intermediate_tensor_names(self): ...
    def last_updated(self): ...
    def dirty_variables(self): ...
    def is_placeholder(self, graph_element_name: Any): ...
    def placeholders(self): ...
    def get_tensor_value(self, tensor_name: Any): ...
    def override_names(self): ...
