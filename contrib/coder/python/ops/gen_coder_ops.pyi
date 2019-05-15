# Stubs for tensorflow.contrib.coder.python.ops.gen_coder_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def pmf_to_quantized_cdf(pmf: Any, precision: Any, name: Optional[Any] = ...): ...
def pmf_to_quantized_cdf_eager_fallback(pmf: Any, precision: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def range_decode(encoded: Any, shape: Any, cdf: Any, precision: Any, name: Optional[Any] = ...): ...
def range_decode_eager_fallback(encoded: Any, shape: Any, cdf: Any, precision: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def range_encode(data: Any, cdf: Any, precision: Any, name: Optional[Any] = ...): ...
def range_encode_eager_fallback(data: Any, cdf: Any, precision: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...