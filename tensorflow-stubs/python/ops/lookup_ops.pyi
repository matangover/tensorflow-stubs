# Stubs for tensorflow.python.ops.lookup_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops.gen_lookup_ops import *
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_lookup_ops as gen_lookup_ops, math_ops as math_ops, string_ops as string_ops
from tensorflow.python.util import compat as compat
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def initialize_all_tables(name: str = ...): ...
def tables_initializer(name: str = ...): ...

class LookupInterface:
    def __init__(self, key_dtype: Any, value_dtype: Any, name: Any) -> None: ...
    @property
    def key_dtype(self): ...
    @property
    def value_dtype(self): ...
    @property
    def name(self): ...
    @property
    def init(self) -> None: ...
    def size(self, name: Optional[Any] = ...) -> None: ...
    def lookup(self, keys: Any, name: Optional[Any] = ...) -> None: ...

class InitializableLookupTableBase(LookupInterface):
    def __init__(self, table_ref: Any, default_value: Any, initializer: Any) -> None: ...
    @property
    def table_ref(self): ...
    @property
    def default_value(self): ...
    @property
    def init(self): ...
    def size(self, name: Optional[Any] = ...): ...
    def lookup(self, keys: Any, name: Optional[Any] = ...): ...

class HashTable(InitializableLookupTableBase):
    def __init__(self, initializer: Any, default_value: Any, shared_name: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def export(self, name: Optional[Any] = ...): ...

class TableInitializerBase:
    def __init__(self, key_dtype: Any, value_dtype: Any) -> None: ...
    @property
    def key_dtype(self): ...
    @property
    def value_dtype(self): ...
    def initialize(self, table: Any) -> None: ...

class KeyValueTensorInitializer(TableInitializerBase):
    def __init__(self, keys: Any, values: Any, key_dtype: Optional[Any] = ..., value_dtype: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def initialize(self, table: Any): ...

class TextFileIndex:
    WHOLE_LINE: int = ...
    LINE_NUMBER: int = ...

class TextFileInitializer(TableInitializerBase):
    def __init__(self, filename: Any, key_dtype: Any, key_index: Any, value_dtype: Any, value_index: Any, vocab_size: Optional[Any] = ..., delimiter: str = ..., name: Optional[Any] = ...) -> None: ...
    def initialize(self, table: Any): ...

class TextFileStringTableInitializer(TextFileInitializer):
    def __init__(self, filename: Any, key_column_index: Any = ..., value_column_index: Any = ..., vocab_size: Optional[Any] = ..., delimiter: str = ..., name: str = ...) -> None: ...

class TextFileIdTableInitializer(TextFileInitializer):
    def __init__(self, filename: Any, key_column_index: Any = ..., value_column_index: Any = ..., vocab_size: Optional[Any] = ..., delimiter: str = ..., name: str = ..., key_dtype: Any = ...) -> None: ...

class HasherSpec: ...

FastHashSpec: Any

class StrongHashSpec(HasherSpec):
    def __new__(cls, key: Any): ...

class IdTableWithHashBuckets(LookupInterface):
    def __init__(self, table: Any, num_oov_buckets: Any, hasher_spec: Any = ..., name: Optional[Any] = ..., key_dtype: Optional[Any] = ...) -> None: ...
    @property
    def init(self): ...
    @property
    def table_ref(self): ...
    def size(self, name: Optional[Any] = ...): ...
    def lookup(self, keys: Any, name: Optional[Any] = ...): ...

def index_table_from_file(vocabulary_file: Optional[Any] = ..., num_oov_buckets: int = ..., vocab_size: Optional[Any] = ..., default_value: int = ..., hasher_spec: Any = ..., key_dtype: Any = ..., name: Optional[Any] = ..., key_column_index: Any = ..., value_column_index: Any = ..., delimiter: str = ...): ...
def index_table_from_tensor(vocabulary_list: Any, num_oov_buckets: int = ..., default_value: int = ..., hasher_spec: Any = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def index_to_string_table_from_file(vocabulary_file: Any, vocab_size: Optional[Any] = ..., default_value: str = ..., name: Optional[Any] = ..., key_column_index: Any = ..., value_column_index: Any = ..., delimiter: str = ...): ...
def index_to_string_table_from_tensor(vocabulary_list: Any, default_value: str = ..., name: Optional[Any] = ...): ...
