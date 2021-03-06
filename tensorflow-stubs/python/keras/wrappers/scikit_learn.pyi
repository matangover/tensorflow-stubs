# Stubs for tensorflow.python.keras.wrappers.scikit_learn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.keras.models import Sequential as Sequential
from tensorflow.python.keras.utils.generic_utils import has_arg as has_arg
from tensorflow.python.keras.utils.np_utils import to_categorical as to_categorical
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class BaseWrapper:
    build_fn: Any = ...
    sk_params: Any = ...
    def __init__(self, build_fn: Optional[Any] = ..., **sk_params: Any) -> None: ...
    def check_params(self, params: Any) -> None: ...
    def get_params(self, **params: Any): ...
    def set_params(self, **params: Any): ...
    model: Any = ...
    def fit(self, x: Any, y: Any, **kwargs: Any): ...
    def filter_sk_params(self, fn: Any, override: Optional[Any] = ...): ...

class KerasClassifier(BaseWrapper):
    classes_: Any = ...
    n_classes_: Any = ...
    def fit(self, x: Any, y: Any, **kwargs: Any): ...
    def predict(self, x: Any, **kwargs: Any): ...
    def predict_proba(self, x: Any, **kwargs: Any): ...
    def score(self, x: Any, y: Any, **kwargs: Any): ...

class KerasRegressor(BaseWrapper):
    def predict(self, x: Any, **kwargs: Any): ...
    def score(self, x: Any, y: Any, **kwargs: Any): ...
