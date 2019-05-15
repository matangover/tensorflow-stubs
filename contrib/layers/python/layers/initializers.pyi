# Stubs for tensorflow.contrib.layers.python.layers.initializers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.ops import random_ops as random_ops
from typing import Any as Any, Optional as Optional

def xavier_initializer(uniform: bool = ..., seed: Optional[Any] = ..., dtype: Any = ...): ...
xavier_initializer_conv2d = xavier_initializer

def variance_scaling_initializer(factor: float = ..., mode: str = ..., uniform: bool = ..., seed: Optional[Any] = ..., dtype: Any = ...): ...