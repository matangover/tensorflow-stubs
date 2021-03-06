# Stubs for tensorflow.contrib.ffmpeg.ops.gen_decode_audio_op_py (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def decode_audio(contents: Any, file_format: Any, samples_per_second: Any, channel_count: Any, name: Optional[Any] = ...): ...
def decode_audio_eager_fallback(contents: Any, file_format: Any, samples_per_second: Any, channel_count: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def decode_audio_v2(contents: Any, file_format: Any, samples_per_second: Any, channel_count: Any, stream: str = ..., name: Optional[Any] = ...): ...
def decode_audio_v2_eager_fallback(contents: Any, file_format: Any, samples_per_second: Any, channel_count: Any, stream: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
