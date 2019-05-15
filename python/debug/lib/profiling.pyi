# Stubs for tensorflow.python.debug.lib.profiling (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any

class ProfileDatum:
    device_name: Any = ...
    node_exec_stats: Any = ...
    file_path: Any = ...
    line_number: Any = ...
    func_name: Any = ...
    file_line_func: Any = ...
    op_type: Any = ...
    start_time: Any = ...
    op_time: Any = ...
    def __init__(self, device_name: Any, node_exec_stats: Any, file_path: Any, line_number: Any, func_name: Any, op_type: Any) -> None: ...
    @property
    def exec_time(self): ...

class AggregateProfile:
    total_op_time: Any = ...
    total_exec_time: Any = ...
    def __init__(self, profile_datum: Any) -> None: ...
    def add(self, profile_datum: Any) -> None: ...
    @property
    def node_count(self): ...
    @property
    def node_exec_count(self): ...