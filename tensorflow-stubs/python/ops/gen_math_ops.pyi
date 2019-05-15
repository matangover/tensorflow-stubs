# Stubs for tensorflow.python.ops.gen_math_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def accumulate_nv2(inputs: Any, shape: Any, name: Optional[Any] = ...): ...
def accumulate_nv2_eager_fallback(inputs: Any, shape: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def acos(x: Any, name: Optional[Any] = ...): ...
def acos_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def acosh(x: Any, name: Optional[Any] = ...): ...
def acosh_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def add(x: Any, y: Any, name: Optional[Any] = ...): ...
def add_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def add_n(inputs: Any, name: Optional[Any] = ...): ...
def add_n_eager_fallback(inputs: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def add_v2(x: Any, y: Any, name: Optional[Any] = ...): ...
def add_v2_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def angle(input: Any, Tout: Any = ..., name: Optional[Any] = ...): ...
def angle_eager_fallback(input: Any, Tout: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def approximate_equal(x: Any, y: Any, tolerance: float = ..., name: Optional[Any] = ...): ...
def approximate_equal_eager_fallback(x: Any, y: Any, tolerance: float = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def arg_max(input: Any, dimension: Any, output_type: Any = ..., name: Optional[Any] = ...): ...
def arg_max_eager_fallback(input: Any, dimension: Any, output_type: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def arg_min(input: Any, dimension: Any, output_type: Any = ..., name: Optional[Any] = ...): ...
def arg_min_eager_fallback(input: Any, dimension: Any, output_type: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def asin(x: Any, name: Optional[Any] = ...): ...
def asin_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def asinh(x: Any, name: Optional[Any] = ...): ...
def asinh_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def atan(x: Any, name: Optional[Any] = ...): ...
def atan_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def atan2(y: Any, x: Any, name: Optional[Any] = ...): ...
def atan2_eager_fallback(y: Any, x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def atanh(x: Any, name: Optional[Any] = ...): ...
def atanh_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def batch_mat_mul(x: Any, y: Any, adj_x: bool = ..., adj_y: bool = ..., name: Optional[Any] = ...): ...
def batch_mat_mul_eager_fallback(x: Any, y: Any, adj_x: bool = ..., adj_y: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def bessel_i0e(x: Any, name: Optional[Any] = ...): ...
def bessel_i0e_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def bessel_i1e(x: Any, name: Optional[Any] = ...): ...
def bessel_i1e_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def betainc(a: Any, b: Any, x: Any, name: Optional[Any] = ...): ...
def betainc_eager_fallback(a: Any, b: Any, x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def bincount(arr: Any, size: Any, weights: Any, name: Optional[Any] = ...): ...
def bincount_eager_fallback(arr: Any, size: Any, weights: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def bucketize(input: Any, boundaries: Any, name: Optional[Any] = ...): ...
def bucketize_eager_fallback(input: Any, boundaries: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def cast(x: Any, DstT: Any, Truncate: bool = ..., name: Optional[Any] = ...): ...
def cast_eager_fallback(x: Any, DstT: Any, Truncate: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def ceil(x: Any, name: Optional[Any] = ...): ...
def ceil_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def compare_and_bitpack(input: Any, threshold: Any, name: Optional[Any] = ...): ...
def compare_and_bitpack_eager_fallback(input: Any, threshold: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def complex_abs(x: Any, Tout: Any = ..., name: Optional[Any] = ...): ...
def complex_abs_eager_fallback(x: Any, Tout: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conj(input: Any, name: Optional[Any] = ...): ...
def conj_eager_fallback(input: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def cos(x: Any, name: Optional[Any] = ...): ...
def cos_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def cosh(x: Any, name: Optional[Any] = ...): ...
def cosh_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def cross(a: Any, b: Any, name: Optional[Any] = ...): ...
def cross_eager_fallback(a: Any, b: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def cumprod(x: Any, axis: Any, exclusive: bool = ..., reverse: bool = ..., name: Optional[Any] = ...): ...
def cumprod_eager_fallback(x: Any, axis: Any, exclusive: bool = ..., reverse: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def cumsum(x: Any, axis: Any, exclusive: bool = ..., reverse: bool = ..., name: Optional[Any] = ...): ...
def cumsum_eager_fallback(x: Any, axis: Any, exclusive: bool = ..., reverse: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def digamma(x: Any, name: Optional[Any] = ...): ...
def digamma_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def div(x: Any, y: Any, name: Optional[Any] = ...): ...
def div_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def div_no_nan(x: Any, y: Any, name: Optional[Any] = ...): ...
def div_no_nan_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def equal(x: Any, y: Any, name: Optional[Any] = ...): ...
def equal_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def erf(x: Any, name: Optional[Any] = ...): ...
def erf_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def erfc(x: Any, name: Optional[Any] = ...): ...
def erfc_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def exp(x: Any, name: Optional[Any] = ...): ...
def exp_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def expm1(x: Any, name: Optional[Any] = ...): ...
def expm1_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def floor(x: Any, name: Optional[Any] = ...): ...
def floor_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def floor_div(x: Any, y: Any, name: Optional[Any] = ...): ...
def floor_div_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def floor_mod(x: Any, y: Any, name: Optional[Any] = ...): ...
def floor_mod_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def greater(x: Any, y: Any, name: Optional[Any] = ...): ...
def greater_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def greater_equal(x: Any, y: Any, name: Optional[Any] = ...): ...
def greater_equal_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def igamma(a: Any, x: Any, name: Optional[Any] = ...): ...
def igamma_eager_fallback(a: Any, x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def igamma_grad_a(a: Any, x: Any, name: Optional[Any] = ...): ...
def igamma_grad_a_eager_fallback(a: Any, x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def igammac(a: Any, x: Any, name: Optional[Any] = ...): ...
def igammac_eager_fallback(a: Any, x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def imag(input: Any, Tout: Any = ..., name: Optional[Any] = ...): ...
def imag_eager_fallback(input: Any, Tout: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def inv(x: Any, name: Optional[Any] = ...): ...
def inv_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def inv_grad(y: Any, dy: Any, name: Optional[Any] = ...): ...
def inv_grad_eager_fallback(y: Any, dy: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def is_finite(x: Any, name: Optional[Any] = ...): ...
def is_finite_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def is_inf(x: Any, name: Optional[Any] = ...): ...
def is_inf_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def is_nan(x: Any, name: Optional[Any] = ...): ...
def is_nan_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def less(x: Any, y: Any, name: Optional[Any] = ...): ...
def less_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def less_equal(x: Any, y: Any, name: Optional[Any] = ...): ...
def less_equal_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lgamma(x: Any, name: Optional[Any] = ...): ...
def lgamma_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lin_space(start: Any, stop: Any, num: Any, name: Optional[Any] = ...): ...
def lin_space_eager_fallback(start: Any, stop: Any, num: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def log(x: Any, name: Optional[Any] = ...): ...
def log_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def log1p(x: Any, name: Optional[Any] = ...): ...
def log1p_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def logical_and(x: Any, y: Any, name: Optional[Any] = ...): ...
def logical_and_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def logical_not(x: Any, name: Optional[Any] = ...): ...
def logical_not_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def logical_or(x: Any, y: Any, name: Optional[Any] = ...): ...
def logical_or_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def mat_mul(a: Any, b: Any, transpose_a: bool = ..., transpose_b: bool = ..., name: Optional[Any] = ...): ...
def mat_mul_eager_fallback(a: Any, b: Any, transpose_a: bool = ..., transpose_b: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def maximum(x: Any, y: Any, name: Optional[Any] = ...): ...
def maximum_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def mean(input: Any, axis: Any, keep_dims: bool = ..., name: Optional[Any] = ...): ...
def mean_eager_fallback(input: Any, axis: Any, keep_dims: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def minimum(x: Any, y: Any, name: Optional[Any] = ...): ...
def minimum_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def mod(x: Any, y: Any, name: Optional[Any] = ...): ...
def mod_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def mul(x: Any, y: Any, name: Optional[Any] = ...): ...
def mul_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def neg(x: Any, name: Optional[Any] = ...): ...
def neg_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def not_equal(x: Any, y: Any, name: Optional[Any] = ...): ...
def not_equal_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def polygamma(a: Any, x: Any, name: Optional[Any] = ...): ...
def polygamma_eager_fallback(a: Any, x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def prod(input: Any, axis: Any, keep_dims: bool = ..., name: Optional[Any] = ...): ...
def prod_eager_fallback(input: Any, axis: Any, keep_dims: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizeDownAndShrinkRangeOutput = namedtuple('QuantizeDownAndShrinkRange', <ERROR>)

def quantize_down_and_shrink_range(input: Any, input_min: Any, input_max: Any, out_type: Any, name: Optional[Any] = ...): ...
def quantize_down_and_shrink_range_eager_fallback(input: Any, input_min: Any, input_max: Any, out_type: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedAddOutput = namedtuple('QuantizedAdd', <ERROR>)

def quantized_add(x: Any, y: Any, min_x: Any, max_x: Any, min_y: Any, max_y: Any, Toutput: Any = ..., name: Optional[Any] = ...): ...
def quantized_add_eager_fallback(x: Any, y: Any, min_x: Any, max_x: Any, min_y: Any, max_y: Any, Toutput: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedMatMulOutput = namedtuple('QuantizedMatMul', <ERROR>)

def quantized_mat_mul(a: Any, b: Any, min_a: Any, max_a: Any, min_b: Any, max_b: Any, Toutput: Any = ..., transpose_a: bool = ..., transpose_b: bool = ..., Tactivation: Any = ..., name: Optional[Any] = ...): ...
def quantized_mat_mul_eager_fallback(a: Any, b: Any, min_a: Any, max_a: Any, min_b: Any, max_b: Any, Toutput: Any = ..., transpose_a: bool = ..., transpose_b: bool = ..., Tactivation: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedMulOutput = namedtuple('QuantizedMul', <ERROR>)

def quantized_mul(x: Any, y: Any, min_x: Any, max_x: Any, min_y: Any, max_y: Any, Toutput: Any = ..., name: Optional[Any] = ...): ...
def quantized_mul_eager_fallback(x: Any, y: Any, min_x: Any, max_x: Any, min_y: Any, max_y: Any, Toutput: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def real(input: Any, Tout: Any = ..., name: Optional[Any] = ...): ...
def real_eager_fallback(input: Any, Tout: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def real_div(x: Any, y: Any, name: Optional[Any] = ...): ...
def real_div_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def reciprocal(x: Any, name: Optional[Any] = ...): ...
def reciprocal_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def reciprocal_grad(y: Any, dy: Any, name: Optional[Any] = ...): ...
def reciprocal_grad_eager_fallback(y: Any, dy: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _RequantizationRangeOutput = namedtuple('RequantizationRange', <ERROR>)

def requantization_range(input: Any, input_min: Any, input_max: Any, name: Optional[Any] = ...): ...
def requantization_range_eager_fallback(input: Any, input_min: Any, input_max: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _RequantizeOutput = namedtuple('Requantize', <ERROR>)

def requantize(input: Any, input_min: Any, input_max: Any, requested_output_min: Any, requested_output_max: Any, out_type: Any, name: Optional[Any] = ...): ...
def requantize_eager_fallback(input: Any, input_min: Any, input_max: Any, requested_output_min: Any, requested_output_max: Any, out_type: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def rint(x: Any, name: Optional[Any] = ...): ...
def rint_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def round(x: Any, name: Optional[Any] = ...): ...
def round_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def rsqrt(x: Any, name: Optional[Any] = ...): ...
def rsqrt_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def rsqrt_grad(y: Any, dy: Any, name: Optional[Any] = ...): ...
def rsqrt_grad_eager_fallback(y: Any, dy: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def segment_max(data: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def segment_max_eager_fallback(data: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def segment_mean(data: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def segment_mean_eager_fallback(data: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def segment_min(data: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def segment_min_eager_fallback(data: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def segment_prod(data: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def segment_prod_eager_fallback(data: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def segment_sum(data: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def segment_sum_eager_fallback(data: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def select(condition: Any, x: Any, y: Any, name: Optional[Any] = ...): ...
def select_eager_fallback(condition: Any, x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sigmoid(x: Any, name: Optional[Any] = ...): ...
def sigmoid_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sigmoid_grad(y: Any, dy: Any, name: Optional[Any] = ...): ...
def sigmoid_grad_eager_fallback(y: Any, dy: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sign(x: Any, name: Optional[Any] = ...): ...
def sign_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sin(x: Any, name: Optional[Any] = ...): ...
def sin_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sinh(x: Any, name: Optional[Any] = ...): ...
def sinh_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_mat_mul(a: Any, b: Any, transpose_a: bool = ..., transpose_b: bool = ..., a_is_sparse: bool = ..., b_is_sparse: bool = ..., name: Optional[Any] = ...): ...
def sparse_mat_mul_eager_fallback(a: Any, b: Any, transpose_a: bool = ..., transpose_b: bool = ..., a_is_sparse: bool = ..., b_is_sparse: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_mean(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def sparse_segment_mean_eager_fallback(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_mean_grad(grad: Any, indices: Any, segment_ids: Any, output_dim0: Any, name: Optional[Any] = ...): ...
def sparse_segment_mean_grad_eager_fallback(grad: Any, indices: Any, segment_ids: Any, output_dim0: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_mean_with_num_segments(data: Any, indices: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def sparse_segment_mean_with_num_segments_eager_fallback(data: Any, indices: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_sqrt_n(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def sparse_segment_sqrt_n_eager_fallback(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_sqrt_n_grad(grad: Any, indices: Any, segment_ids: Any, output_dim0: Any, name: Optional[Any] = ...): ...
def sparse_segment_sqrt_n_grad_eager_fallback(grad: Any, indices: Any, segment_ids: Any, output_dim0: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_sqrt_n_with_num_segments(data: Any, indices: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def sparse_segment_sqrt_n_with_num_segments_eager_fallback(data: Any, indices: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_sum(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ...): ...
def sparse_segment_sum_eager_fallback(data: Any, indices: Any, segment_ids: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_segment_sum_with_num_segments(data: Any, indices: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def sparse_segment_sum_with_num_segments_eager_fallback(data: Any, indices: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sqrt(x: Any, name: Optional[Any] = ...): ...
def sqrt_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sqrt_grad(y: Any, dy: Any, name: Optional[Any] = ...): ...
def sqrt_grad_eager_fallback(y: Any, dy: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def square(x: Any, name: Optional[Any] = ...): ...
def square_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def squared_difference(x: Any, y: Any, name: Optional[Any] = ...): ...
def squared_difference_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sub(x: Any, y: Any, name: Optional[Any] = ...): ...
def sub_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def tan(x: Any, name: Optional[Any] = ...): ...
def tan_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def tanh(x: Any, name: Optional[Any] = ...): ...
def tanh_eager_fallback(x: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def tanh_grad(y: Any, dy: Any, name: Optional[Any] = ...): ...
def tanh_grad_eager_fallback(y: Any, dy: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def truncate_div(x: Any, y: Any, name: Optional[Any] = ...): ...
def truncate_div_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def truncate_mod(x: Any, y: Any, name: Optional[Any] = ...): ...
def truncate_mod_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def unsorted_segment_max(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def unsorted_segment_max_eager_fallback(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def unsorted_segment_min(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def unsorted_segment_min_eager_fallback(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def unsorted_segment_prod(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def unsorted_segment_prod_eager_fallback(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def unsorted_segment_sum(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ...): ...
def unsorted_segment_sum_eager_fallback(data: Any, segment_ids: Any, num_segments: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def xdivy(x: Any, y: Any, name: Optional[Any] = ...): ...
def xdivy_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def xlogy(x: Any, y: Any, name: Optional[Any] = ...): ...
def xlogy_eager_fallback(x: Any, y: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def zeta(x: Any, q: Any, name: Optional[Any] = ...): ...
def zeta_eager_fallback(x: Any, q: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...