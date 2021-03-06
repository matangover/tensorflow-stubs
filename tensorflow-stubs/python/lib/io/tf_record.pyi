# Stubs for tensorflow.python.lib.io.tf_record (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.framework import errors as errors
from tensorflow.python.util import compat as compat, deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class TFRecordCompressionType:
    NONE: int = ...
    ZLIB: int = ...
    GZIP: int = ...

class TFRecordOptions:
    compression_type_map: Any = ...
    compression_type: Any = ...
    flush_mode: Any = ...
    input_buffer_size: Any = ...
    output_buffer_size: Any = ...
    window_bits: Any = ...
    compression_level: Any = ...
    compression_method: Any = ...
    mem_level: Any = ...
    compression_strategy: Any = ...
    def __init__(self, compression_type: Optional[Any] = ..., flush_mode: Optional[Any] = ..., input_buffer_size: Optional[Any] = ..., output_buffer_size: Optional[Any] = ..., window_bits: Optional[Any] = ..., compression_level: Optional[Any] = ..., compression_method: Optional[Any] = ..., mem_level: Optional[Any] = ..., compression_strategy: Optional[Any] = ...) -> None: ...
    @classmethod
    def get_compression_type_string(cls, options: Any): ...

def tf_record_iterator(path: Any, options: Optional[Any] = ...) -> None: ...

class TFRecordWriter:
    def __init__(self, path: Any, options: Optional[Any] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, unused_type: Any, unused_value: Any, unused_traceback: Any) -> None: ...
    def write(self, record: Any) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
