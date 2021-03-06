# Stubs for tensorflow.contrib.graph_editor.util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any, Optional as Optional

class ListView:
    def __init__(self, list_: Any) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __getitem__(self, i: Any): ...
    def __add__(self, other: Any): ...

def make_list_of_op(ops: Any, check_graph: bool = ..., allow_graph: bool = ..., ignore_ts: bool = ...): ...
def get_tensors(graph: Any): ...
def make_list_of_t(ts: Any, check_graph: bool = ..., allow_graph: bool = ..., ignore_ops: bool = ...): ...
def get_generating_ops(ts: Any): ...
def get_consuming_ops(ts: Any): ...

class ControlOutputs:
    def __init__(self, graph: Any) -> None: ...
    def update(self): ...
    def get_all(self): ...
    def get(self, op: Any): ...
    @property
    def graph(self): ...

def placeholder_name(t: Optional[Any] = ..., scope: Optional[Any] = ..., prefix: Any = ...): ...
def make_placeholder_from_tensor(t: Any, scope: Optional[Any] = ..., prefix: Any = ...): ...
def make_placeholder_from_dtype_and_shape(dtype: Any, shape: Optional[Any] = ..., scope: Optional[Any] = ..., prefix: Any = ...): ...
