# Stubs for tensorflow.python.ops.math_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops.gen_math_ops import *
from tensorflow.python.eager import context as context
from tensorflow.python.framework import common_shapes as common_shapes, constant_op as constant_op, dtypes as dtypes, graph_util as graph_util, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_data_flow_ops as gen_data_flow_ops, gen_math_ops as gen_math_ops, gen_nn_ops as gen_nn_ops, gen_sparse_ops as gen_sparse_ops, gen_spectral_ops as gen_spectral_ops
from tensorflow.python.util import compat as compat, deprecation as deprecation, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

linspace = gen_math_ops.lin_space
arg_max: Any
arg_min: Any

def argmax(input: Any, axis: Optional[Any] = ..., name: Optional[Any] = ..., dimension: Optional[Any] = ..., output_type: Any = ...): ...
def argmin(input: Any, axis: Optional[Any] = ..., name: Optional[Any] = ..., dimension: Optional[Any] = ..., output_type: Any = ...): ...
def abs(x: Any, name: Optional[Any] = ...): ...

class DivideDelegateWithName:
    x: Any = ...
    name: Any = ...
    def __init__(self, x: Any, name: Any) -> None: ...
    def __truediv__(self, y: Any): ...
    def __floordiv__(self, y: Any): ...
    def __div__(self, y: Any): ...

def divide(x: Any, y: Any, name: Optional[Any] = ...): ...
def multiply(x: Any, y: Any, name: Optional[Any] = ...): ...
def subtract(x: Any, y: Any, name: Optional[Any] = ...): ...
def negative(x: Any, name: Optional[Any] = ...): ...
def sign(x: Any, name: Optional[Any] = ...): ...
def square(x: Any, name: Optional[Any] = ...): ...
def sqrt(x: Any, name: Optional[Any] = ...): ...
def erf(x: Any, name: Optional[Any] = ...): ...
def scalar_mul(scalar: Any, x: Any): ...
def pow(x: Any, y: Any, name: Optional[Any] = ...): ...
def complex(real: Any, imag: Any, name: Optional[Any] = ...): ...
def real(input: Any, name: Optional[Any] = ...): ...
def imag(input: Any, name: Optional[Any] = ...): ...
def angle(input: Any, name: Optional[Any] = ...): ...
def round(x: Any, name: Optional[Any] = ...): ...
def cast(x: Any, dtype: Any, name: Optional[Any] = ...): ...
def saturate_cast(value: Any, dtype: Any, name: Optional[Any] = ...): ...
def to_float(x: Any, name: str = ...): ...
def to_double(x: Any, name: str = ...): ...
def to_int32(x: Any, name: str = ...): ...
def to_int64(x: Any, name: str = ...): ...
def to_bfloat16(x: Any, name: str = ...): ...
def to_complex64(x: Any, name: str = ...): ...
def to_complex128(x: Any, name: str = ...): ...
def truediv(x: Any, y: Any, name: Optional[Any] = ...): ...
def div(x: Any, y: Any, name: Optional[Any] = ...): ...
def div_no_nan(x: Any, y: Any, name: Optional[Any] = ...): ...
mod = gen_math_ops.floor_mod

def floordiv(x: Any, y: Any, name: Optional[Any] = ...): ...
realdiv = gen_math_ops.real_div
truncatediv = gen_math_ops.truncate_div
floor_div = gen_math_ops.floor_div
truncatemod = gen_math_ops.truncate_mod
floormod = gen_math_ops.floor_mod

def logical_xor(x: Any, y: Any, name: str = ...): ...
def range(start: Any, limit: Optional[Any] = ..., delta: int = ..., dtype: Optional[Any] = ..., name: str = ...): ...
def reduce_sum(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def count_nonzero(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., dtype: Any = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def reduce_mean(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def reduce_prod(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def reduce_min(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def reduce_max(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def reduce_all(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def reduce_any(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def reduce_logsumexp(input_tensor: Any, axis: Optional[Any] = ..., keepdims: Optional[Any] = ..., name: Optional[Any] = ..., reduction_indices: Optional[Any] = ..., keep_dims: Optional[Any] = ...): ...
def trace(x: Any, name: Optional[Any] = ...): ...
def matmul(a: Any, b: Any, transpose_a: bool = ..., transpose_b: bool = ..., adjoint_a: bool = ..., adjoint_b: bool = ..., a_is_sparse: bool = ..., b_is_sparse: bool = ..., name: Optional[Any] = ...): ...
sparse_matmul = gen_math_ops.sparse_mat_mul

def add_n(inputs: Any, name: Optional[Any] = ...): ...
def accumulate_n(inputs: Any, shape: Optional[Any] = ..., tensor_dtype: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sigmoid(x: Any, name: Optional[Any] = ...): ...
def log_sigmoid(x: Any, name: Optional[Any] = ...): ...
def tanh(x: Any, name: Optional[Any] = ...): ...
def bincount(arr: Any, weights: Optional[Any] = ..., minlength: Optional[Any] = ..., maxlength: Optional[Any] = ..., dtype: Any = ...): ...
def cumsum(x: Any, axis: int = ..., exclusive: bool = ..., reverse: bool = ..., name: Optional[Any] = ...): ...
def cumprod(x: Any, axis: int = ..., exclusive: bool = ..., reverse: bool = ..., name: Optional[Any] = ...): ...
def conj(x: Any, name: Optional[Any] = ...): ...
def reduced_shape(input_shape: Any, axes: Any): ...
def unsorted_segment_mean(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def unsorted_segment_sqrt_n(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def sparse_segment_sum(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ..., num_segments: Optional[Any] = ...): ...
def sparse_segment_mean(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ..., num_segments: Optional[Any] = ...): ...
def sparse_segment_sqrt_n(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ..., num_segments: Optional[Any] = ...): ...
def tensordot(a: Any, b: Any, axes: Any, name: Optional[Any] = ...): ...
def polyval(coeffs: Any, x: Any, name: Optional[Any] = ...): ...
def bessel_i0e(x: Any, name: Optional[Any] = ...): ...
def bessel_i1e(x: Any, name: Optional[Any] = ...): ...
fft = gen_spectral_ops.fft
ifft = gen_spectral_ops.ifft
fft2d = gen_spectral_ops.fft2d
ifft2d = gen_spectral_ops.ifft2d
fft3d = gen_spectral_ops.fft3d
ifft3d = gen_spectral_ops.ifft3d
