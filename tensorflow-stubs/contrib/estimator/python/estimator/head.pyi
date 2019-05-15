# Stubs for tensorflow.contrib.estimator.python.estimator.head (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.estimator import model_fn as model_fn
from tensorflow.python.estimator.canned import head as head_lib, metric_keys as metric_keys, prediction_keys as prediction_keys
from tensorflow.python.estimator.export import export_output as export_output
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, lookup_ops as lookup_ops, math_ops as math_ops, nn as nn, sparse_ops as sparse_ops
from tensorflow.python.ops.losses import losses as losses
from tensorflow.python.saved_model import signature_constants as signature_constants
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import training_util as training_util
from typing import Any as Any, Optional as Optional

def multi_class_head(n_classes: Any, weight_column: Optional[Any] = ..., label_vocabulary: Optional[Any] = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., name: Optional[Any] = ...): ...
def binary_classification_head(weight_column: Optional[Any] = ..., thresholds: Optional[Any] = ..., label_vocabulary: Optional[Any] = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., name: Optional[Any] = ...): ...
def regression_head(weight_column: Optional[Any] = ..., label_dimension: int = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., inverse_link_fn: Optional[Any] = ..., name: Optional[Any] = ...): ...
def poisson_regression_head(weight_column: Optional[Any] = ..., label_dimension: int = ..., loss_reduction: Any = ..., compute_full_loss: bool = ..., name: Optional[Any] = ...): ...
def logistic_regression_head(weight_column: Optional[Any] = ..., loss_reduction: Any = ..., name: Optional[Any] = ...): ...
def multi_label_head(n_classes: Any, weight_column: Optional[Any] = ..., thresholds: Optional[Any] = ..., label_vocabulary: Optional[Any] = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., classes_for_class_based_metrics: Optional[Any] = ..., name: Optional[Any] = ...): ...

class _MultiLabelHead(head_lib._Head):
    def __init__(self, n_classes: Any, weight_column: Optional[Any] = ..., thresholds: Optional[Any] = ..., label_vocabulary: Optional[Any] = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., classes_for_class_based_metrics: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def logits_dimension(self): ...
    def create_loss(self, features: Any, mode: Any, logits: Any, labels: Any): ...