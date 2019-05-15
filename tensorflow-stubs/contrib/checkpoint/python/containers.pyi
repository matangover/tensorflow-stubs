# Stubs for tensorflow.contrib.checkpoint.python.containers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.training.checkpointable import data_structures as data_structures
from typing import Any as Any

class UniqueNameTracker(data_structures.CheckpointableDataStructure):
    def __init__(self) -> None: ...
    def track(self, checkpointable: Any, base_name: Any): ...