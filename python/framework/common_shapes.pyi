# Stubs for tensorflow.python.framework.common_shapes (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.framework import cpp_shape_inference_pb2 as cpp_shape_inference_pb2, errors as errors, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from typing import Any as Any

def has_fully_defined_shape(tensor: Any): ...
def rank(tensor: Any): ...
def scalar_shape(unused_op: Any): ...
def unchanged_shape(op: Any): ...
def unchanged_shape_with_rank(rank: Any): ...
def unchanged_shape_with_rank_at_least(rank: Any): ...
def unchanged_shape_with_rank_at_most(rank: Any): ...
def matmul_shape(op: Any): ...
def get_conv_output_size(input_size: Any, filter_size: Any, strides: Any, padding_type: Any): ...
def get2d_conv_output_size(input_height: Any, input_width: Any, filter_height: Any, filter_width: Any, row_stride: Any, col_stride: Any, padding_type: Any): ...
def conv2d_shape(op: Any): ...
def depthwise_conv2d_native_shape(op: Any): ...
def separable_conv2d_shape(op: Any): ...
def avg_pool_shape(op: Any): ...
def max_pool_shape(op: Any): ...
def no_outputs(unused_op: Any): ...
def unknown_shape(op: Any): ...
def is_broadcast_compatible(shape_x: Any, shape_y: Any): ...
def broadcast_shape(shape_x: Any, shape_y: Any): ...
def call_cpp_shape_fn(op: Any, require_shape_fn: bool = ...): ...
