# Stubs for tensorflow.contrib.ffmpeg.ops.gen_encode_audio_op_py (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def encode_audio(sampled_audio: Any, file_format: Any, samples_per_second: Any, bits_per_second: int = ..., name: Optional[Any] = ...): ...
def encode_audio_eager_fallback(sampled_audio: Any, file_format: Any, samples_per_second: Any, bits_per_second: int = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def encode_audio_v2(sampled_audio: Any, file_format: Any, samples_per_second: Any, bits_per_second: Any, name: Optional[Any] = ...): ...
def encode_audio_v2_eager_fallback(sampled_audio: Any, file_format: Any, samples_per_second: Any, bits_per_second: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
