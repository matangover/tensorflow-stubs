# Stubs for tensorflow.python.data.ops.readers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class TextLineDataset(dataset_ops.Dataset):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ...) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class _TFRecordDataset(dataset_ops.Dataset):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ...) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class ParallelInterleaveDataset(dataset_ops.InterleaveDataset):
    def __init__(self, input_dataset: Any, map_func: Any, cycle_length: Any, block_length: Any, sloppy: Any, buffer_output_elements: Any, prefetch_input_elements: Any) -> None: ...

class TFRecordDataset(dataset_ops.Dataset):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ...) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class FixedLengthRecordDataset(dataset_ops.Dataset):
    def __init__(self, filenames: Any, record_bytes: Any, header_bytes: Optional[Any] = ..., footer_bytes: Optional[Any] = ..., buffer_size: Optional[Any] = ...) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
