# Stubs for tensorflow.python.keras.utils.conv_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.keras import backend as backend
from typing import Any as Any

def convert_data_format(data_format: Any, ndim: Any): ...
def normalize_tuple(value: Any, n: Any, name: Any): ...
def conv_output_length(input_length: Any, filter_size: Any, padding: Any, stride: Any, dilation: int = ...): ...
def conv_input_length(output_length: Any, filter_size: Any, padding: Any, stride: Any): ...
def deconv_output_length(input_length: Any, filter_size: Any, padding: Any, stride: Any): ...
def normalize_data_format(value: Any): ...
def normalize_padding(value: Any): ...
def convert_kernel(kernel: Any): ...
def conv_kernel_mask(input_shape: Any, kernel_shape: Any, strides: Any, padding: Any): ...
def conv_connected_inputs(input_shape: Any, kernel_shape: Any, output_position: Any, strides: Any, padding: Any): ...
def conv_output_shape(input_shape: Any, kernel_shape: Any, strides: Any, padding: Any): ...
