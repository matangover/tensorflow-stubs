# Stubs for tensorflow.python.ops.gen_nn_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def avg_pool(value: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def avg_pool_eager_fallback(value: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def avg_pool3d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def avg_pool3d_eager_fallback(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def avg_pool3d_grad(orig_input_shape: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def avg_pool3d_grad_eager_fallback(orig_input_shape: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def avg_pool_grad(orig_input_shape: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def avg_pool_grad_eager_fallback(orig_input_shape: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _BatchNormWithGlobalNormalizationGradOutput = namedtuple('BatchNormWithGlobalNormalizationGrad', <ERROR>)

def batch_norm_with_global_normalization_grad(t: Any, m: Any, v: Any, gamma: Any, backprop: Any, variance_epsilon: Any, scale_after_normalization: Any, name: Optional[Any] = ...): ...
def batch_norm_with_global_normalization_grad_eager_fallback(t: Any, m: Any, v: Any, gamma: Any, backprop: Any, variance_epsilon: Any, scale_after_normalization: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def bias_add(value: Any, bias: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def bias_add_eager_fallback(value: Any, bias: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def bias_add_grad(out_backprop: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def bias_add_grad_eager_fallback(out_backprop: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def bias_add_v1(value: Any, bias: Any, name: Optional[Any] = ...): ...
def bias_add_v1_eager_fallback(value: Any, bias: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv2d(input: Any, filter: Any, strides: Any, padding: Any, use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def conv2d_eager_fallback(input: Any, filter: Any, strides: Any, padding: Any, use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv2d_backprop_filter(input: Any, filter_sizes: Any, out_backprop: Any, strides: Any, padding: Any, use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def conv2d_backprop_filter_eager_fallback(input: Any, filter_sizes: Any, out_backprop: Any, strides: Any, padding: Any, use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv2d_backprop_input(input_sizes: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def conv2d_backprop_input_eager_fallback(input_sizes: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv3d(input: Any, filter: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def conv3d_eager_fallback(input: Any, filter: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv3d_backprop_filter(input: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, dilations: Any = ..., name: Optional[Any] = ...): ...
def conv3d_backprop_filter_eager_fallback(input: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv3d_backprop_filter_v2(input: Any, filter_sizes: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def conv3d_backprop_filter_v2_eager_fallback(input: Any, filter_sizes: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv3d_backprop_input(input: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, dilations: Any = ..., name: Optional[Any] = ...): ...
def conv3d_backprop_input_eager_fallback(input: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def conv3d_backprop_input_v2(input_sizes: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def conv3d_backprop_input_v2_eager_fallback(input_sizes: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def data_format_dim_map(x: Any, src_format: str = ..., dst_format: str = ..., name: Optional[Any] = ...): ...
def data_format_dim_map_eager_fallback(x: Any, src_format: str = ..., dst_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def data_format_vec_permute(x: Any, src_format: str = ..., dst_format: str = ..., name: Optional[Any] = ...): ...
def data_format_vec_permute_eager_fallback(x: Any, src_format: str = ..., dst_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def depthwise_conv2d_native(input: Any, filter: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def depthwise_conv2d_native_eager_fallback(input: Any, filter: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def depthwise_conv2d_native_backprop_filter(input: Any, filter_sizes: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def depthwise_conv2d_native_backprop_filter_eager_fallback(input: Any, filter_sizes: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def depthwise_conv2d_native_backprop_input(input_sizes: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def depthwise_conv2d_native_backprop_input_eager_fallback(input_sizes: Any, filter: Any, out_backprop: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def dilation2d(input: Any, filter: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ...): ...
def dilation2d_eager_fallback(input: Any, filter: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def dilation2d_backprop_filter(input: Any, filter: Any, out_backprop: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ...): ...
def dilation2d_backprop_filter_eager_fallback(input: Any, filter: Any, out_backprop: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def dilation2d_backprop_input(input: Any, filter: Any, out_backprop: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ...): ...
def dilation2d_backprop_input_eager_fallback(input: Any, filter: Any, out_backprop: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def elu(features: Any, name: Optional[Any] = ...): ...
def elu_eager_fallback(features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def elu_grad(gradients: Any, outputs: Any, name: Optional[Any] = ...): ...
def elu_grad_eager_fallback(gradients: Any, outputs: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _FractionalAvgPoolOutput = namedtuple('FractionalAvgPool', <ERROR>)

def fractional_avg_pool(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...
def fractional_avg_pool_eager_fallback(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def fractional_avg_pool_grad(orig_input_tensor_shape: Any, out_backprop: Any, row_pooling_sequence: Any, col_pooling_sequence: Any, overlapping: bool = ..., name: Optional[Any] = ...): ...
def fractional_avg_pool_grad_eager_fallback(orig_input_tensor_shape: Any, out_backprop: Any, row_pooling_sequence: Any, col_pooling_sequence: Any, overlapping: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _FractionalMaxPoolOutput = namedtuple('FractionalMaxPool', <ERROR>)

def fractional_max_pool(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...
def fractional_max_pool_eager_fallback(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def fractional_max_pool_grad(orig_input: Any, orig_output: Any, out_backprop: Any, row_pooling_sequence: Any, col_pooling_sequence: Any, overlapping: bool = ..., name: Optional[Any] = ...): ...
def fractional_max_pool_grad_eager_fallback(orig_input: Any, orig_output: Any, out_backprop: Any, row_pooling_sequence: Any, col_pooling_sequence: Any, overlapping: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _FusedBatchNormOutput = namedtuple('FusedBatchNorm', <ERROR>)

# _FusedBatchNormGradOutput = namedtuple('FusedBatchNormGrad', <ERROR>)

def fused_batch_norm_grad(y_backprop: Any, x: Any, scale: Any, reserve_space_1: Any, reserve_space_2: Any, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Optional[Any] = ...): ...
def fused_batch_norm_grad_eager_fallback(y_backprop: Any, x: Any, scale: Any, reserve_space_1: Any, reserve_space_2: Any, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _FusedBatchNormGradV2Output = namedtuple('FusedBatchNormGradV2', <ERROR>)

def fused_batch_norm_grad_v2(y_backprop: Any, x: Any, scale: Any, reserve_space_1: Any, reserve_space_2: Any, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Optional[Any] = ...): ...
def fused_batch_norm_grad_v2_eager_fallback(y_backprop: Any, x: Any, scale: Any, reserve_space_1: Any, reserve_space_2: Any, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _FusedBatchNormV2Output = namedtuple('FusedBatchNormV2', <ERROR>)

def fused_batch_norm_v2(x: Any, scale: Any, offset: Any, mean: Any, variance: Any, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Optional[Any] = ...): ...
def fused_batch_norm_v2_eager_fallback(x: Any, scale: Any, offset: Any, mean: Any, variance: Any, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def fused_pad_conv2d(input: Any, paddings: Any, filter: Any, mode: Any, strides: Any, padding: Any, name: Optional[Any] = ...): ...
def fused_pad_conv2d_eager_fallback(input: Any, paddings: Any, filter: Any, mode: Any, strides: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def fused_resize_and_pad_conv2d(input: Any, size: Any, paddings: Any, filter: Any, mode: Any, strides: Any, padding: Any, resize_align_corners: bool = ..., name: Optional[Any] = ...): ...
def fused_resize_and_pad_conv2d_eager_fallback(input: Any, size: Any, paddings: Any, filter: Any, mode: Any, strides: Any, padding: Any, resize_align_corners: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def in_top_k(predictions: Any, targets: Any, k: Any, name: Optional[Any] = ...): ...
def in_top_k_eager_fallback(predictions: Any, targets: Any, k: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def in_top_kv2(predictions: Any, targets: Any, k: Any, name: Optional[Any] = ...): ...
def in_top_kv2_eager_fallback(predictions: Any, targets: Any, k: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def l2_loss(t: Any, name: Optional[Any] = ...): ...
def l2_loss_eager_fallback(t: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lrn(input: Any, depth_radius: int = ..., bias: int = ..., alpha: int = ..., beta: float = ..., name: Optional[Any] = ...): ...
def lrn_eager_fallback(input: Any, depth_radius: int = ..., bias: int = ..., alpha: int = ..., beta: float = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lrn_grad(input_grads: Any, input_image: Any, output_image: Any, depth_radius: int = ..., bias: int = ..., alpha: int = ..., beta: float = ..., name: Optional[Any] = ...): ...
def lrn_grad_eager_fallback(input_grads: Any, input_image: Any, output_image: Any, depth_radius: int = ..., bias: int = ..., alpha: int = ..., beta: float = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def log_softmax(logits: Any, name: Optional[Any] = ...): ...
def log_softmax_eager_fallback(logits: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_eager_fallback(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool3d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool3d_eager_fallback(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool3d_grad(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool3d_grad_eager_fallback(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool3d_grad_grad(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool3d_grad_grad_eager_fallback(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool_grad(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_grad_eager_fallback(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool_grad_grad(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_grad_grad_eager_fallback(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool_grad_grad_v2(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_grad_grad_v2_eager_fallback(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool_grad_grad_with_argmax(input: Any, grad: Any, argmax: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ...): ...
def max_pool_grad_grad_with_argmax_eager_fallback(input: Any, grad: Any, argmax: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool_grad_v2(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_grad_v2_eager_fallback(orig_input: Any, orig_output: Any, grad: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool_grad_with_argmax(input: Any, grad: Any, argmax: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ...): ...
def max_pool_grad_with_argmax_eager_fallback(input: Any, grad: Any, argmax: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def max_pool_v2(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_v2_eager_fallback(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _MaxPoolWithArgmaxOutput = namedtuple('MaxPoolWithArgmax', <ERROR>)

def max_pool_with_argmax(input: Any, ksize: Any, strides: Any, padding: Any, Targmax: Any = ..., name: Optional[Any] = ...): ...
def max_pool_with_argmax_eager_fallback(input: Any, ksize: Any, strides: Any, padding: Any, Targmax: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def nth_element(input: Any, n: Any, reverse: bool = ..., name: Optional[Any] = ...): ...
def nth_element_eager_fallback(input: Any, n: Any, reverse: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedAvgPoolOutput = namedtuple('QuantizedAvgPool', <ERROR>)

def quantized_avg_pool(input: Any, min_input: Any, max_input: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ...): ...
def quantized_avg_pool_eager_fallback(input: Any, min_input: Any, max_input: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedBatchNormWithGlobalNormalizationOutput = namedtuple('QuantizedBatchNormWithGlobalNormalization', <ERROR>)

def quantized_batch_norm_with_global_normalization(t: Any, t_min: Any, t_max: Any, m: Any, m_min: Any, m_max: Any, v: Any, v_min: Any, v_max: Any, beta: Any, beta_min: Any, beta_max: Any, gamma: Any, gamma_min: Any, gamma_max: Any, out_type: Any, variance_epsilon: Any, scale_after_normalization: Any, name: Optional[Any] = ...): ...
def quantized_batch_norm_with_global_normalization_eager_fallback(t: Any, t_min: Any, t_max: Any, m: Any, m_min: Any, m_max: Any, v: Any, v_min: Any, v_max: Any, beta: Any, beta_min: Any, beta_max: Any, gamma: Any, gamma_min: Any, gamma_max: Any, out_type: Any, variance_epsilon: Any, scale_after_normalization: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedBiasAddOutput = namedtuple('QuantizedBiasAdd', <ERROR>)

def quantized_bias_add(input: Any, bias: Any, min_input: Any, max_input: Any, min_bias: Any, max_bias: Any, out_type: Any, name: Optional[Any] = ...): ...
def quantized_bias_add_eager_fallback(input: Any, bias: Any, min_input: Any, max_input: Any, min_bias: Any, max_bias: Any, out_type: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedConv2DOutput = namedtuple('QuantizedConv2D', <ERROR>)

def quantized_conv2d(input: Any, filter: Any, min_input: Any, max_input: Any, min_filter: Any, max_filter: Any, strides: Any, padding: Any, out_type: Any = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def quantized_conv2d_eager_fallback(input: Any, filter: Any, min_input: Any, max_input: Any, min_filter: Any, max_filter: Any, strides: Any, padding: Any, out_type: Any = ..., dilations: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedMaxPoolOutput = namedtuple('QuantizedMaxPool', <ERROR>)

def quantized_max_pool(input: Any, min_input: Any, max_input: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ...): ...
def quantized_max_pool_eager_fallback(input: Any, min_input: Any, max_input: Any, ksize: Any, strides: Any, padding: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedReluOutput = namedtuple('QuantizedRelu', <ERROR>)

def quantized_relu(features: Any, min_features: Any, max_features: Any, out_type: Any = ..., name: Optional[Any] = ...): ...
def quantized_relu_eager_fallback(features: Any, min_features: Any, max_features: Any, out_type: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedRelu6Output = namedtuple('QuantizedRelu6', <ERROR>)

def quantized_relu6(features: Any, min_features: Any, max_features: Any, out_type: Any = ..., name: Optional[Any] = ...): ...
def quantized_relu6_eager_fallback(features: Any, min_features: Any, max_features: Any, out_type: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _QuantizedReluXOutput = namedtuple('QuantizedReluX', <ERROR>)

def quantized_relu_x(features: Any, max_value: Any, min_features: Any, max_features: Any, out_type: Any = ..., name: Optional[Any] = ...): ...
def quantized_relu_x_eager_fallback(features: Any, max_value: Any, min_features: Any, max_features: Any, out_type: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def relu(features: Any, name: Optional[Any] = ...): ...
def relu_eager_fallback(features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def relu6(features: Any, name: Optional[Any] = ...): ...
def relu6_eager_fallback(features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def relu6_grad(gradients: Any, features: Any, name: Optional[Any] = ...): ...
def relu6_grad_eager_fallback(gradients: Any, features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def relu_grad(gradients: Any, features: Any, name: Optional[Any] = ...): ...
def relu_grad_eager_fallback(gradients: Any, features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def selu(features: Any, name: Optional[Any] = ...): ...
def selu_eager_fallback(features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def selu_grad(gradients: Any, outputs: Any, name: Optional[Any] = ...): ...
def selu_grad_eager_fallback(gradients: Any, outputs: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def softmax(logits: Any, name: Optional[Any] = ...): ...
def softmax_eager_fallback(logits: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _SoftmaxCrossEntropyWithLogitsOutput = namedtuple('SoftmaxCrossEntropyWithLogits', <ERROR>)

def softmax_cross_entropy_with_logits(features: Any, labels: Any, name: Optional[Any] = ...): ...
def softmax_cross_entropy_with_logits_eager_fallback(features: Any, labels: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def softplus(features: Any, name: Optional[Any] = ...): ...
def softplus_eager_fallback(features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def softplus_grad(gradients: Any, features: Any, name: Optional[Any] = ...): ...
def softplus_grad_eager_fallback(gradients: Any, features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def softsign(features: Any, name: Optional[Any] = ...): ...
def softsign_eager_fallback(features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def softsign_grad(gradients: Any, features: Any, name: Optional[Any] = ...): ...
def softsign_grad_eager_fallback(gradients: Any, features: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _SparseSoftmaxCrossEntropyWithLogitsOutput = namedtuple('SparseSoftmaxCrossEntropyWithLogits', <ERROR>)

def sparse_softmax_cross_entropy_with_logits(features: Any, labels: Any, name: Optional[Any] = ...): ...
def sparse_softmax_cross_entropy_with_logits_eager_fallback(features: Any, labels: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _TopKOutput = namedtuple('TopK', <ERROR>)

def top_k(input: Any, k: Any, sorted: bool = ..., name: Optional[Any] = ...): ...
def top_k_eager_fallback(input: Any, k: Any, sorted: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _TopKV2Output = namedtuple('TopKV2', <ERROR>)

def top_kv2(input: Any, k: Any, sorted: bool = ..., name: Optional[Any] = ...): ...
def top_kv2_eager_fallback(input: Any, k: Any, sorted: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
