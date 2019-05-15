# Stubs for tensorflow.contrib.data.python.ops.readers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.experimental.ops import optimization as optimization, readers as readers
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

def make_csv_dataset(file_pattern: Any, batch_size: Any, column_names: Optional[Any] = ..., column_defaults: Optional[Any] = ..., label_name: Optional[Any] = ..., select_columns: Optional[Any] = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., header: bool = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Any = ..., num_parallel_reads: int = ..., sloppy: bool = ..., num_rows_for_inference: int = ..., compression_type: Optional[Any] = ...): ...

class CsvDataset(readers.CsvDataset):
    def __init__(self, filenames: Any, record_defaults: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., header: bool = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols: Optional[Any] = ...) -> None: ...

def make_batched_features_dataset(file_pattern: Any, batch_size: Any, features: Any, reader: Any = ..., label_key: Optional[Any] = ..., reader_args: Optional[Any] = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Any = ..., reader_num_threads: int = ..., parser_num_threads: int = ..., sloppy_ordering: bool = ..., drop_final_batch: bool = ...): ...
def read_batch_features(file_pattern: Any, batch_size: Any, features: Any, reader: Any = ..., reader_args: Optional[Any] = ..., randomize_input: bool = ..., num_epochs: Optional[Any] = ..., capacity: int = ...): ...

class SqlDataset(readers.SqlDataset):
    def __init__(self, driver_name: Any, data_source_name: Any, query: Any, output_types: Any) -> None: ...

class LMDBDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any) -> None: ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...