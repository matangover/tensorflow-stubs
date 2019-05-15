# Stubs for tensorflow.contrib.kafka.python.ops.kafka_dataset_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.kafka.python.ops import gen_dataset_ops as gen_dataset_ops, kafka_op_loader as kafka_op_loader
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from typing import Any as Any

class KafkaDataset(dataset_ops.DatasetSource):
    def __init__(self, topics: Any, servers: str = ..., group: str = ..., eof: bool = ..., timeout: int = ...) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
