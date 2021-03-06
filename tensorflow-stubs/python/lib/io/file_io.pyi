# Stubs for tensorflow.python.lib.io.file_io (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.framework import c_api_util as c_api_util, errors as errors
from tensorflow.python.util import compat as compat, deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class FileIO:
    def __init__(self, name: Any, mode: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def mode(self): ...
    def size(self): ...
    def write(self, file_content: Any) -> None: ...
    def read(self, n: int = ...): ...
    def seek(self, offset: Optional[Any] = ..., whence: int = ..., position: Optional[Any] = ...) -> None: ...
    def readline(self): ...
    def readlines(self): ...
    def tell(self): ...
    def __enter__(self): ...
    def __exit__(self, unused_type: Any, unused_value: Any, unused_traceback: Any) -> None: ...
    def __iter__(self): ...
    def next(self): ...
    def __next__(self): ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

def file_exists(filename: Any): ...
def delete_file(filename: Any) -> None: ...
def read_file_to_string(filename: Any, binary_mode: bool = ...): ...
def write_string_to_file(filename: Any, file_content: Any) -> None: ...
def get_matching_files(filename: Any): ...
def create_dir(dirname: Any) -> None: ...
def recursive_create_dir(dirname: Any) -> None: ...
def copy(oldpath: Any, newpath: Any, overwrite: bool = ...) -> None: ...
def rename(oldname: Any, newname: Any, overwrite: bool = ...) -> None: ...
def atomic_write_string_to_file(filename: Any, contents: Any, overwrite: bool = ...) -> None: ...
def delete_recursively(dirname: Any) -> None: ...
def is_directory(dirname: Any): ...
def list_directory(dirname: Any): ...
def walk(top: Any, in_order: bool = ...) -> None: ...
def stat(filename: Any): ...
def filecmp(filename_a: Any, filename_b: Any): ...
def file_crc32(filename: Any, block_size: Any = ...): ...
