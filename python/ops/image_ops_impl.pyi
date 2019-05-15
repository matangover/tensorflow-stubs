# Stubs for tensorflow.python.ops.image_ops_impl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.compat import compat as compat
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_image_ops as gen_image_ops, gen_nn_ops as gen_nn_ops, math_ops as math_ops, nn as nn, nn_ops as nn_ops, random_ops as random_ops, string_ops as string_ops, variables as variables
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def fix_image_flip_shape(image: Any, result: Any): ...
def random_flip_up_down(image: Any, seed: Optional[Any] = ...): ...
def random_flip_left_right(image: Any, seed: Optional[Any] = ...): ...
def flip_left_right(image: Any): ...
def flip_up_down(image: Any): ...
def rot90(image: Any, k: int = ..., name: Optional[Any] = ...): ...
def transpose_image(image: Any): ...
def central_crop(image: Any, central_fraction: Any): ...
def pad_to_bounding_box(image: Any, offset_height: Any, offset_width: Any, target_height: Any, target_width: Any): ...
def crop_to_bounding_box(image: Any, offset_height: Any, offset_width: Any, target_height: Any, target_width: Any): ...
def resize_image_with_crop_or_pad(image: Any, target_height: Any, target_width: Any): ...

class ResizeMethod:
    BILINEAR: int = ...
    NEAREST_NEIGHBOR: int = ...
    BICUBIC: int = ...
    AREA: int = ...

def resize_images(images: Any, size: Any, method: Any = ..., align_corners: bool = ..., preserve_aspect_ratio: bool = ...): ...
def resize_image_with_pad(image: Any, target_height: Any, target_width: Any, method: Any = ...): ...
def per_image_standardization(image: Any): ...
def random_brightness(image: Any, max_delta: Any, seed: Optional[Any] = ...): ...
def random_contrast(image: Any, lower: Any, upper: Any, seed: Optional[Any] = ...): ...
def adjust_brightness(image: Any, delta: Any): ...
def adjust_contrast(images: Any, contrast_factor: Any): ...
def adjust_gamma(image: Any, gamma: int = ..., gain: int = ...): ...
def convert_image_dtype(image: Any, dtype: Any, saturate: bool = ..., name: Optional[Any] = ...): ...
def rgb_to_grayscale(images: Any, name: Optional[Any] = ...): ...
def grayscale_to_rgb(images: Any, name: Optional[Any] = ...): ...
def random_hue(image: Any, max_delta: Any, seed: Optional[Any] = ...): ...
def adjust_hue(image: Any, delta: Any, name: Optional[Any] = ...): ...
def random_jpeg_quality(image: Any, min_jpeg_quality: Any, max_jpeg_quality: Any, seed: Optional[Any] = ...): ...
def adjust_jpeg_quality(image: Any, jpeg_quality: Any, name: Optional[Any] = ...): ...
def random_saturation(image: Any, lower: Any, upper: Any, seed: Optional[Any] = ...): ...
def adjust_saturation(image: Any, saturation_factor: Any, name: Optional[Any] = ...): ...
def is_jpeg(contents: Any, name: Optional[Any] = ...): ...
def decode_image(contents: Any, channels: Optional[Any] = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def total_variation(images: Any, name: Optional[Any] = ...): ...
def sample_distorted_bounding_box(image_size: Any, bounding_boxes: Any, seed: Optional[Any] = ..., seed2: Optional[Any] = ..., min_object_covered: float = ..., aspect_ratio_range: Optional[Any] = ..., area_range: Optional[Any] = ..., max_attempts: Optional[Any] = ..., use_image_if_no_bounding_boxes: Optional[Any] = ..., name: Optional[Any] = ...): ...
def non_max_suppression(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: float = ..., score_threshold: Any = ..., name: Optional[Any] = ...): ...
def non_max_suppression_padded(boxes: Any, scores: Any, max_output_size: Any, iou_threshold: float = ..., score_threshold: Any = ..., pad_to_max_output_size: bool = ..., name: Optional[Any] = ...): ...
def non_max_suppression_with_overlaps(overlaps: Any, scores: Any, max_output_size: Any, overlap_threshold: float = ..., score_threshold: Any = ..., name: Optional[Any] = ...): ...
def rgb_to_yiq(images: Any): ...
def yiq_to_rgb(images: Any): ...
def rgb_to_yuv(images: Any): ...
def yuv_to_rgb(images: Any): ...
def psnr(a: Any, b: Any, max_val: Any, name: Optional[Any] = ...): ...
def ssim(img1: Any, img2: Any, max_val: Any): ...
def ssim_multiscale(img1: Any, img2: Any, max_val: Any, power_factors: Any = ...): ...
def image_gradients(image: Any): ...
def sobel_edges(image: Any): ...