# Stubs for tensorflow.python.training.coordinator (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import threading as threading
from tensorflow.python.framework import errors as errors
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class Coordinator:
    def __init__(self, clean_stop_exception_types: Optional[Any] = ...) -> None: ...
    def request_stop(self, ex: Optional[Any] = ...) -> None: ...
    def clear_stop(self) -> None: ...
    def should_stop(self): ...
    def stop_on_exception(self) -> None: ...
    def wait_for_stop(self, timeout: Optional[Any] = ...): ...
    def register_thread(self, thread: Any) -> None: ...
    def join(self, threads: Optional[Any] = ..., stop_grace_period_secs: int = ..., ignore_live_threads: bool = ...) -> None: ...
    @property
    def joined(self): ...
    def raise_requested_exception(self) -> None: ...

class LooperThread(threading.Thread):
    daemon: bool = ...
    def __init__(self, coord: Any, timer_interval_secs: Any, target: Optional[Any] = ..., args: Optional[Any] = ..., kwargs: Optional[Any] = ...) -> None: ...
    @staticmethod
    def loop(coord: Any, timer_interval_secs: Any, target: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ...): ...
    def run(self) -> None: ...
    def start_loop(self) -> None: ...
    def stop_loop(self) -> None: ...
    def run_loop(self) -> None: ...
