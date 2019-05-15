# Stubs for tensorflow.python.data.experimental.ops.scan_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest, sparse as sparse
from tensorflow.python.framework import ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

class _ScanDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, initial_state: Any, scan_func: Any) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

def scan(initial_state: Any, scan_func: Any): ...
