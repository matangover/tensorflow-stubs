# Stubs for tensorflow.python.ops.gen_logging_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def audio_summary(tag: Any, tensor: Any, sample_rate: Any, max_outputs: int = ..., name: Optional[Any] = ...): ...
def audio_summary_eager_fallback(tag: Any, tensor: Any, sample_rate: Any, max_outputs: int = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def audio_summary_v2(tag: Any, tensor: Any, sample_rate: Any, max_outputs: int = ..., name: Optional[Any] = ...): ...
def audio_summary_v2_eager_fallback(tag: Any, tensor: Any, sample_rate: Any, max_outputs: int = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def histogram_summary(tag: Any, values: Any, name: Optional[Any] = ...): ...
def histogram_summary_eager_fallback(tag: Any, values: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def image_summary(tag: Any, tensor: Any, max_images: int = ..., bad_color: Any = ..., name: Optional[Any] = ...): ...
def image_summary_eager_fallback(tag: Any, tensor: Any, max_images: int = ..., bad_color: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def merge_summary(inputs: Any, name: Optional[Any] = ...): ...
def merge_summary_eager_fallback(inputs: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def print_v2(input: Any, output_stream: str = ..., name: Optional[Any] = ...): ...
def print_v2_eager_fallback(input: Any, output_stream: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def scalar_summary(tags: Any, values: Any, name: Optional[Any] = ...): ...
def scalar_summary_eager_fallback(tags: Any, values: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def tensor_summary(tensor: Any, description: str = ..., labels: Any = ..., display_name: str = ..., name: Optional[Any] = ...): ...
def tensor_summary_eager_fallback(tensor: Any, description: str = ..., labels: Any = ..., display_name: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def tensor_summary_v2(tag: Any, tensor: Any, serialized_summary_metadata: Any, name: Optional[Any] = ...): ...
def tensor_summary_v2_eager_fallback(tag: Any, tensor: Any, serialized_summary_metadata: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def timestamp(name: Optional[Any] = ...): ...
def timestamp_eager_fallback(name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
