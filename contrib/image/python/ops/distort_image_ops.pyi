# Stubs for tensorflow.contrib.image.python.ops.distort_image_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.image.ops import gen_distort_image_ops as gen_distort_image_ops
from tensorflow.contrib.util import loader as loader
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import image_ops as image_ops, random_ops as random_ops
from tensorflow.python.platform import resource_loader as resource_loader
from typing import Any as Any, Optional as Optional

def random_hsv_in_yiq(image: Any, max_delta_hue: int = ..., lower_saturation: int = ..., upper_saturation: int = ..., lower_value: int = ..., upper_value: int = ..., seed: Optional[Any] = ...): ...
def adjust_hsv_in_yiq(image: Any, delta_hue: int = ..., scale_saturation: int = ..., scale_value: int = ..., name: Optional[Any] = ...): ...
