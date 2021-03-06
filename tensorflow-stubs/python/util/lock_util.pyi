# Stubs for tensorflow.python.util.lock_util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any

class GroupLock:
    def __init__(self, num_groups: int = ...) -> None: ...
    def group(self, group_id: Any): ...
    def acquire(self, group_id: Any) -> None: ...
    def release(self, group_id: Any) -> None: ...
    class _Context:
        def __init__(self, lock: Any, group_id: Any) -> None: ...
        def __enter__(self) -> None: ...
        def __exit__(self, type_arg: Any, value_arg: Any, traceback_arg: Any) -> None: ...
