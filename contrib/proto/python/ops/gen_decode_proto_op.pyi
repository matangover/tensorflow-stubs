# Stubs for tensorflow.contrib.proto.python.ops.gen_decode_proto_op (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

# _DecodeProtoV2Output = namedtuple('DecodeProtoV2', <ERROR>)

def decode_proto_v2(bytes: Any, message_type: Any, field_names: Any, output_types: Any, descriptor_source: str = ..., message_format: str = ..., sanitize: bool = ..., name: Optional[Any] = ...): ...
def decode_proto_v2_eager_fallback(bytes: Any, message_type: Any, field_names: Any, output_types: Any, descriptor_source: str = ..., message_format: str = ..., sanitize: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...