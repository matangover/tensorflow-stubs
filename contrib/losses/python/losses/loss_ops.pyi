# Stubs for tensorflow.contrib.losses.python.losses.loss_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.framework.python.ops import add_arg_scope as add_arg_scope
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn, nn_ops as nn_ops
from tensorflow.python.util.deprecation import deprecated as deprecated, deprecated_args as deprecated_args, deprecated_argument_lookup as deprecated_argument_lookup
from typing import Any as Any, Optional as Optional

def compute_weighted_loss(losses: Any, weights: float = ..., scope: Optional[Any] = ...): ...
def add_loss(loss: Any, loss_collection: Any = ...) -> None: ...
def get_losses(scope: Optional[Any] = ..., loss_collection: Any = ...): ...
def get_regularization_losses(scope: Optional[Any] = ...): ...
def get_total_loss(add_regularization_losses: bool = ..., name: str = ...): ...
def absolute_difference(predictions: Any, labels: Optional[Any] = ..., weights: float = ..., scope: Optional[Any] = ...): ...
def sigmoid_cross_entropy(logits: Any, multi_class_labels: Any, weights: float = ..., label_smoothing: int = ..., scope: Optional[Any] = ...): ...
def softmax_cross_entropy(logits: Any, onehot_labels: Any, weights: float = ..., label_smoothing: int = ..., scope: Optional[Any] = ...): ...
def sparse_softmax_cross_entropy(logits: Any, labels: Any, weights: float = ..., scope: Optional[Any] = ...): ...
def log_loss(predictions: Any, labels: Optional[Any] = ..., weights: float = ..., epsilon: float = ..., scope: Optional[Any] = ...): ...
def hinge_loss(logits: Any, labels: Optional[Any] = ..., scope: Optional[Any] = ...): ...
def mean_squared_error(predictions: Any, labels: Optional[Any] = ..., weights: float = ..., scope: Optional[Any] = ...): ...
def mean_pairwise_squared_error(predictions: Any, labels: Optional[Any] = ..., weights: float = ..., scope: Optional[Any] = ...): ...
def cosine_distance(predictions: Any, labels: Optional[Any] = ..., axis: Optional[Any] = ..., weights: float = ..., scope: Optional[Any] = ..., dim: Optional[Any] = ...): ...
