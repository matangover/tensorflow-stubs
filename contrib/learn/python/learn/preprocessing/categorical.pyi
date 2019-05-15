# Stubs for tensorflow.contrib.learn.python.learn.preprocessing.categorical (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any as Any, Optional as Optional

class CategoricalProcessor:
    min_frequency: Any = ...
    share: Any = ...
    vocabularies_: Any = ...
    def __init__(self, min_frequency: int = ..., share: bool = ..., vocabularies: Optional[Any] = ...) -> None: ...
    def freeze(self, freeze: bool = ...) -> None: ...
    def fit(self, x: Any, unused_y: Optional[Any] = ...): ...
    def fit_transform(self, x: Any, unused_y: Optional[Any] = ...): ...
    def transform(self, x: Any) -> None: ...