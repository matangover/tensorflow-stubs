# Stubs for tensorflow.contrib.learn.python.learn.preprocessing.categorical_vocabulary (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any as Any

class CategoricalVocabulary:
    def __init__(self, unknown_token: str = ..., support_reverse: bool = ...) -> None: ...
    def __len__(self): ...
    def freeze(self, freeze: bool = ...) -> None: ...
    def get(self, category: Any): ...
    def add(self, category: Any, count: int = ...) -> None: ...
    def trim(self, min_frequency: Any, max_frequency: int = ...): ...
    def reverse(self, class_id: Any): ...
