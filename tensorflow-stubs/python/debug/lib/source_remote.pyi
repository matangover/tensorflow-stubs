# Stubs for tensorflow.python.debug.lib.source_remote (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.debug import debug_service_pb2 as debug_service_pb2
from tensorflow.core.protobuf import debug_pb2 as debug_pb2
from tensorflow.python.debug.lib import common as common, debug_service_pb2_grpc as debug_service_pb2_grpc, source_utils as source_utils
from tensorflow.python.platform import gfile as gfile, tf_logging as tf_logging
from tensorflow.python.profiler import tfprof_logger as tfprof_logger
from typing import Any as Any

def grpc_message_length_bytes(): ...
def send_graph_tracebacks(destinations: Any, run_key: Any, origin_stack: Any, graph: Any, send_source: bool = ...) -> None: ...
def send_eager_tracebacks(destinations: Any, origin_stack: Any, send_source: bool = ...) -> None: ...
