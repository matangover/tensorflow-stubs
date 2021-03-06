# Stubs for tensorflow.contrib.graph_editor.subgraph (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.graph_editor import select as select, util as util
from typing import Any as Any, Optional as Optional

class SubGraphView:
    def __init__(self, inside_ops: Any = ..., passthrough_ts: Any = ...) -> None: ...
    def __copy__(self): ...
    def copy(self): ...
    def remap_default(self, remove_input_map: bool = ..., remove_output_map: bool = ...): ...
    def remap_outputs_make_unique(self): ...
    def remap_outputs_to_consumers(self): ...
    def remove_unused_ops(self, control_inputs: bool = ...): ...
    def remap_inputs(self, new_input_indices: Any): ...
    def remap_outputs(self, new_output_indices: Any): ...
    def remap(self, new_input_indices: Optional[Any] = ..., new_output_indices: Optional[Any] = ...): ...
    def find_op_by_name(self, op_name: Any): ...
    @property
    def graph(self): ...
    @property
    def ops(self): ...
    @property
    def inputs(self): ...
    @property
    def connected_inputs(self): ...
    @property
    def outputs(self): ...
    @property
    def connected_outputs(self): ...
    @property
    def passthroughs(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def op(self, op_id: Any): ...
    def is_passthrough(self, t: Any): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def input_index(self, t: Any): ...
    def output_index(self, t: Any): ...
    def consumers(self): ...

def make_view(*args: Any, **kwargs: Any): ...
def make_view_from_scope(scope: Any, graph: Any): ...
