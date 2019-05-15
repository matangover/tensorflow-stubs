# Stubs for tensorflow.contrib.kernel_methods.python.mappers.random_fourier_features (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.kernel_methods.python.mappers import dense_kernel_mapper as dkm
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes
from tensorflow.python.ops import math_ops as math_ops
from typing import Any as Any, Optional as Optional

class RandomFourierFeatureMapper(dkm.DenseKernelMapper):
    def __init__(self, input_dim: Any, output_dim: Any, stddev: float = ..., seed: int = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def input_dim(self): ...
    @property
    def output_dim(self): ...
    def map(self, input_tensor: Any): ...
