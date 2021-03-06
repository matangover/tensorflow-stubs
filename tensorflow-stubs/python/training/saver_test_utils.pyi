# Stubs for tensorflow.python.training.saver_test_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.ops import gen_lookup_ops as gen_lookup_ops
from tensorflow.python.training import saver as saver_module
from typing import Any as Any, Optional as Optional

class CheckpointedOp:
    table_ref: Any = ...
    def __init__(self, name: Any, table_ref: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def saveable(self): ...
    def insert(self, keys: Any, values: Any): ...
    def lookup(self, keys: Any, default: Any): ...
    def keys(self): ...
    def values(self): ...
    class CustomSaveable(saver_module.BaseSaverBuilder.SaveableObject):
        def __init__(self, table: Any, name: Any) -> None: ...
        def restore(self, restore_tensors: Any, shapes: Any): ...
