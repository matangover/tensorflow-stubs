# Stubs for tensorflow.contrib.kinesis.python.ops.kinesis_dataset_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.kinesis.python.ops import gen_dataset_ops as gen_dataset_ops, kinesis_op_loader as kinesis_op_loader
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from typing import Any as Any

class KinesisDataset(dataset_ops.DatasetSource):
    def __init__(self, stream: Any, shard: str = ..., read_indefinitely: bool = ..., interval: int = ...) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
