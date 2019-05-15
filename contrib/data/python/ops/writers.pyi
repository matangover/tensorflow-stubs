# Stubs for tensorflow.contrib.data.python.ops.writers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.experimental.ops import writers as writers
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

class TFRecordWriter(writers.TFRecordWriter):
    def __init__(self, filename: Any, compression_type: Optional[Any] = ...) -> None: ...
