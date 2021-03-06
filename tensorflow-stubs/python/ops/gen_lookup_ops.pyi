# Stubs for tensorflow.python.ops.gen_lookup_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def hash_table(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., name: Optional[Any] = ...): ...
def hash_table_v2(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., name: Optional[Any] = ...): ...
def hash_table_v2_eager_fallback(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def initialize_table(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ...): ...
def initialize_table_from_text_file(table_handle: Any, filename: Any, key_index: Any, value_index: Any, vocab_size: int = ..., delimiter: str = ..., name: Optional[Any] = ...): ...
def initialize_table_from_text_file_v2(table_handle: Any, filename: Any, key_index: Any, value_index: Any, vocab_size: int = ..., delimiter: str = ..., name: Optional[Any] = ...): ...
def initialize_table_from_text_file_v2_eager_fallback(table_handle: Any, filename: Any, key_index: Any, value_index: Any, vocab_size: int = ..., delimiter: str = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def initialize_table_v2(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ...): ...
def initialize_table_v2_eager_fallback(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _LookupTableExportOutput = namedtuple('LookupTableExport', <ERROR>)

def lookup_table_export(table_handle: Any, Tkeys: Any, Tvalues: Any, name: Optional[Any] = ...): ...

# _LookupTableExportV2Output = namedtuple('LookupTableExportV2', <ERROR>)

def lookup_table_export_v2(table_handle: Any, Tkeys: Any, Tvalues: Any, name: Optional[Any] = ...): ...
def lookup_table_export_v2_eager_fallback(table_handle: Any, Tkeys: Any, Tvalues: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lookup_table_find(table_handle: Any, keys: Any, default_value: Any, name: Optional[Any] = ...): ...
def lookup_table_find_v2(table_handle: Any, keys: Any, default_value: Any, name: Optional[Any] = ...): ...
def lookup_table_find_v2_eager_fallback(table_handle: Any, keys: Any, default_value: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lookup_table_import(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ...): ...
def lookup_table_import_v2(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ...): ...
def lookup_table_import_v2_eager_fallback(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lookup_table_insert(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ...): ...
def lookup_table_insert_v2(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ...): ...
def lookup_table_insert_v2_eager_fallback(table_handle: Any, keys: Any, values: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def lookup_table_size(table_handle: Any, name: Optional[Any] = ...): ...
def lookup_table_size_v2(table_handle: Any, name: Optional[Any] = ...): ...
def lookup_table_size_v2_eager_fallback(table_handle: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def mutable_dense_hash_table(empty_key: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., value_shape: Any = ..., initial_num_buckets: int = ..., max_load_factor: float = ..., name: Optional[Any] = ...): ...
def mutable_dense_hash_table_v2(empty_key: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., value_shape: Any = ..., initial_num_buckets: int = ..., max_load_factor: float = ..., name: Optional[Any] = ...): ...
def mutable_dense_hash_table_v2_eager_fallback(empty_key: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., value_shape: Any = ..., initial_num_buckets: int = ..., max_load_factor: float = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def mutable_hash_table(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., name: Optional[Any] = ...): ...
def mutable_hash_table_of_tensors(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., value_shape: Any = ..., name: Optional[Any] = ...): ...
def mutable_hash_table_of_tensors_v2(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., value_shape: Any = ..., name: Optional[Any] = ...): ...
def mutable_hash_table_of_tensors_v2_eager_fallback(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., value_shape: Any = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def mutable_hash_table_v2(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., name: Optional[Any] = ...): ...
def mutable_hash_table_v2_eager_fallback(key_dtype: Any, value_dtype: Any, container: str = ..., shared_name: str = ..., use_node_name_sharing: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
