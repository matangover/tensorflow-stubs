# Stubs for tensorflow.python.data.experimental.ops.optimization (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from typing import Any as Any, Optional as Optional

AUTOTUNE: int

def assert_next(transformations: Any): ...
def model(): ...
def optimize(optimizations: Optional[Any] = ...): ...

class _AssertNextDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, transformations: Any) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
