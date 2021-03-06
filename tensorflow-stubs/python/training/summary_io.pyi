# Stubs for tensorflow.python.training.summary_io (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.summary.summary_iterator import summary_iterator as summary_iterator
from tensorflow.python.summary.writer.writer import FileWriter as _FileWriter
from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any as Any, Optional as Optional

class SummaryWriter(_FileWriter):
    def __init__(self, logdir: Any, graph: Optional[Any] = ..., max_queue: int = ..., flush_secs: int = ..., graph_def: Optional[Any] = ...) -> None: ...
