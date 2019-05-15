# Stubs for tensorflow.python.platform.gfile (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.lib.io.file_io import FileIO as _FileIO
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

class GFile(_FileIO):
    def __init__(self, name: Any, mode: str = ...) -> None: ...

class FastGFile(_FileIO):
    def __init__(self, name: Any, mode: str = ...) -> None: ...
Open = GFile