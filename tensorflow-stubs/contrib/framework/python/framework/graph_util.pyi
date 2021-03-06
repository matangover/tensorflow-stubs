# Stubs for tensorflow.contrib.framework.python.framework.graph_util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import graph_pb2 as graph_pb2, node_def_pb2 as node_def_pb2
from tensorflow.python.framework import ops as ops
from tensorflow.python.framework.graph_util_impl import _assert_nodes_are_present as _assert_nodes_are_present, _bfs_for_reachable_nodes as _bfs_for_reachable_nodes, _extract_graph_summary as _extract_graph_summary, _node_name as _node_name
from typing import Any as Any

def fuse_op(graph_def: Any, input_nodes: Any, output_nodes: Any, output_dtypes: Any, output_quantized: Any, op_name: Any, op_type: Any): ...
def get_placeholders(graph: Any): ...
