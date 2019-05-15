# Stubs for tensorflow.python.data.experimental.ops.parsing_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops, parsing_ops as parsing_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

class _ParseExampleDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, features: Any, num_parallel_calls: Any) -> None: ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def output_classes(self): ...

def parse_example_dataset(features: Any, num_parallel_calls: int = ...): ...
