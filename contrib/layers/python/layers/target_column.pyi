# Stubs for tensorflow.contrib.layers.python.layers.target_column (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.framework import deprecated as deprecated
from tensorflow.contrib.losses.python.losses import loss_ops as loss_ops
from tensorflow.contrib.metrics.python.ops import metric_ops as metric_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, nn as nn
from typing import Any as Any, Optional as Optional

def regression_target(label_name: Optional[Any] = ..., weight_column_name: Optional[Any] = ..., label_dimension: int = ...): ...
def multi_class_target(n_classes: Any, label_name: Optional[Any] = ..., weight_column_name: Optional[Any] = ...): ...
def binary_svm_target(label_name: Optional[Any] = ..., weight_column_name: Optional[Any] = ...): ...

class ProblemType:
    UNSPECIFIED: int = ...
    CLASSIFICATION: int = ...
    LINEAR_REGRESSION: int = ...
    LOGISTIC_REGRESSION: int = ...

class _TargetColumn:
    def __init__(self, loss_fn: Any, num_label_columns: Any, label_name: Any, weight_column_name: Any, problem_type: Any) -> None: ...
    def logits_to_predictions(self, logits: Any, proba: bool = ...) -> None: ...
    def get_eval_ops(self, features: Any, logits: Any, labels: Any, metrics: Optional[Any] = ...) -> None: ...
    @property
    def label_name(self): ...
    @property
    def weight_column_name(self): ...
    @property
    def num_label_columns(self): ...
    def get_weight_tensor(self, features: Any): ...
    @property
    def problem_type(self): ...
    def training_loss(self, logits: Any, target: Any, features: Any, name: str = ...): ...
    def loss(self, logits: Any, target: Any, features: Any): ...

class _RegressionTargetColumn(_TargetColumn):
    def __init__(self, loss_fn: Any, label_name: Any, weight_column_name: Any, label_dimension: Any) -> None: ...
    def logits_to_predictions(self, logits: Any, proba: bool = ...): ...
    def get_eval_ops(self, features: Any, logits: Any, labels: Any, metrics: Optional[Any] = ...): ...

class _MultiClassTargetColumn(_TargetColumn):
    def __init__(self, loss_fn: Any, n_classes: Any, label_name: Any, weight_column_name: Any) -> None: ...
    def logits_to_predictions(self, logits: Any, proba: bool = ...): ...
    def get_eval_ops(self, features: Any, logits: Any, labels: Any, metrics: Optional[Any] = ...): ...

class _BinarySvmTargetColumn(_MultiClassTargetColumn):
    def __init__(self, label_name: Any, weight_column_name: Any) -> None: ...
    def logits_to_predictions(self, logits: Any, proba: bool = ...): ...

def get_default_binary_metrics_for_eval(thresholds: Any): ...

class _MetricKeys:
    AUC: str = ...
    PREDICTION_MEAN: str = ...
    TARGET_MEAN: str = ...
    ACCURACY_BASELINE: str = ...
    ACCURACY_MEAN: str = ...
    PRECISION_MEAN: str = ...
    RECALL_MEAN: str = ...