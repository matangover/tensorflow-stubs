# Stubs for tensorflow.contrib.learn.python.learn.estimators.debug (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.layers.python.layers import optimizers as optimizers
from tensorflow.contrib.learn.python.learn.estimators import estimator as estimator, prediction_key as prediction_key
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops
from typing import Any as Any, Optional as Optional

def debug_model_fn(features: Any, labels: Any, mode: Any, params: Any, config: Optional[Any] = ...): ...

class DebugClassifier(estimator.Estimator):
    def __init__(self, model_dir: Optional[Any] = ..., n_classes: int = ..., weight_column_name: Optional[Any] = ..., config: Optional[Any] = ..., feature_engineering_fn: Optional[Any] = ..., label_keys: Optional[Any] = ...) -> None: ...
    def predict_classes(self, input_fn: Optional[Any] = ..., batch_size: Optional[Any] = ...): ...
    def predict_proba(self, input_fn: Optional[Any] = ..., batch_size: Optional[Any] = ...): ...

class DebugRegressor(estimator.Estimator):
    def __init__(self, model_dir: Optional[Any] = ..., label_dimension: int = ..., weight_column_name: Optional[Any] = ..., config: Optional[Any] = ..., feature_engineering_fn: Optional[Any] = ...) -> None: ...
    def predict_scores(self, input_fn: Optional[Any] = ..., batch_size: Optional[Any] = ...): ...
