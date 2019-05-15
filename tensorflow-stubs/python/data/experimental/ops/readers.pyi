# Stubs for tensorflow.python.data.experimental.ops.readers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.experimental.ops import batching as batching, interleave_ops as interleave_ops, optimization as optimization, parsing_ops as parsing_ops, shuffle_ops as shuffle_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert, nest as nest
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops, gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def make_tf_record_dataset(file_pattern: Any, batch_size: Any, parser_fn: Optional[Any] = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: Optional[Any] = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Any = ..., num_parallel_reads: Optional[Any] = ..., num_parallel_parser_calls: Optional[Any] = ..., drop_final_batch: bool = ...): ...
def make_csv_dataset(file_pattern: Any, batch_size: Any, column_names: Optional[Any] = ..., column_defaults: Optional[Any] = ..., label_name: Optional[Any] = ..., select_columns: Optional[Any] = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., header: bool = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Any = ..., num_parallel_reads: int = ..., sloppy: bool = ..., num_rows_for_inference: int = ..., compression_type: Optional[Any] = ...): ...

class CsvDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any, record_defaults: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., header: bool = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols: Optional[Any] = ...) -> None: ...
    @property
    def output_types(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_classes(self): ...

def make_batched_features_dataset(file_pattern: Any, batch_size: Any, features: Any, reader: Any = ..., label_key: Optional[Any] = ..., reader_args: Optional[Any] = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Any = ..., reader_num_threads: int = ..., parser_num_threads: int = ..., sloppy_ordering: bool = ..., drop_final_batch: bool = ...): ...

class SqlDataset(dataset_ops.DatasetSource):
    def __init__(self, driver_name: Any, data_source_name: Any, query: Any, output_types: Any) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...