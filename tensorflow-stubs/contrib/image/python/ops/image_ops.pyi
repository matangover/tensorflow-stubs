# Stubs for tensorflow.contrib.image.python.ops.image_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.image.ops import gen_image_ops as gen_image_ops
from tensorflow.contrib.util import loader as loader
from tensorflow.python.framework import common_shapes as common_shapes, constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, linalg_ops as linalg_ops, math_ops as math_ops
from tensorflow.python.platform import resource_loader as resource_loader
from typing import Any as Any, Optional as Optional

def rotate(images: Any, angles: Any, interpolation: str = ..., name: Optional[Any] = ...): ...
def translate(images: Any, translations: Any, interpolation: str = ..., name: Optional[Any] = ...): ...
def angles_to_projective_transforms(angles: Any, image_height: Any, image_width: Any, name: Optional[Any] = ...): ...
def translations_to_projective_transforms(translations: Any, name: Optional[Any] = ...): ...
def transform(images: Any, transforms: Any, interpolation: str = ..., output_shape: Optional[Any] = ..., name: Optional[Any] = ...): ...
def compose_transforms(*transforms: Any): ...
def flat_transforms_to_matrices(transforms: Any): ...
def matrices_to_flat_transforms(transform_matrices: Any): ...
def bipartite_match(distance_mat: Any, num_valid_rows: Any, top_k: int = ..., name: str = ...): ...
def connected_components(images: Any): ...
