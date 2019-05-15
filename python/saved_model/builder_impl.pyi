# Stubs for tensorflow.python.saved_model.builder_impl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from google.protobuf.any_pb2 import Any as Any
from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2, saved_model_pb2 as saved_model_pb2, saver_pb2 as saver_pb2
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.saved_model import constants as constants
from tensorflow.python.util import compat as compat
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args, deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Optional as Optional

class SavedModelBuilder:
    def __init__(self, export_dir: Any) -> None: ...
    def add_meta_graph(self, tags: Any, signature_def_map: Optional[Any] = ..., assets_collection: Optional[Any] = ..., legacy_init_op: Optional[Any] = ..., clear_devices: bool = ..., main_op: Optional[Any] = ..., strip_default_attrs: bool = ..., saver: Optional[Any] = ...) -> None: ...
    def add_meta_graph_and_variables(self, sess: Any, tags: Any, signature_def_map: Optional[Any] = ..., assets_collection: Optional[Any] = ..., legacy_init_op: Optional[Any] = ..., clear_devices: bool = ..., main_op: Optional[Any] = ..., strip_default_attrs: bool = ..., saver: Optional[Any] = ...) -> None: ...
    def save(self, as_text: bool = ...): ...
