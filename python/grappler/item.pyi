# Stubs for tensorflow.python.grappler.item (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.grappler.costs import op_performance_data_pb2 as op_performance_data_pb2
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2
from tensorflow.python.framework import errors as errors
from typing import Any as Any

class Item:
    def __init__(self, metagraph: Any, ignore_colocation: bool = ..., ignore_user_placement: bool = ...) -> None: ...
    def IdentifyImportantOps(self, sort_topologically: bool = ...): ...
    def GetOpProperties(self): ...
    def GetColocationGroups(self): ...
    @property
    def metagraph(self): ...
    @property
    def tf_item(self): ...
