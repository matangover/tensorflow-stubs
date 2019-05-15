# Stubs for tensorflow.contrib.hadoop.python.ops.hadoop_dataset_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.hadoop.python.ops import gen_dataset_ops as gen_dataset_ops, hadoop_op_loader as hadoop_op_loader
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from typing import Any as Any

class SequenceFileDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...