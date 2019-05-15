# Stubs for tensorflow.python.ops.spectral_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops import gen_spectral_ops as gen_spectral_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

fft = gen_spectral_ops.fft
ifft = gen_spectral_ops.ifft
fft2d = gen_spectral_ops.fft2d
ifft2d = gen_spectral_ops.ifft2d
fft3d = gen_spectral_ops.fft3d
ifft3d = gen_spectral_ops.ifft3d
rfft: Any
irfft: Any
rfft2d: Any
irfft2d: Any
rfft3d: Any
irfft3d: Any

def dct(input: Any, type: int = ..., n: Optional[Any] = ..., axis: int = ..., norm: Optional[Any] = ..., name: Optional[Any] = ...): ...
def idct(input: Any, type: int = ..., n: Optional[Any] = ..., axis: int = ..., norm: Optional[Any] = ..., name: Optional[Any] = ...): ...
