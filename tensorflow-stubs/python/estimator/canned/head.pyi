# Stubs for tensorflow.python.estimator.canned.head (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from collections import namedtuple as namedtuple
from tensorflow.python.estimator import model_fn as model_fn
from tensorflow.python.estimator.canned import metric_keys as metric_keys, prediction_keys as prediction_keys
from tensorflow.python.estimator.export import export_output as export_output
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, lookup_ops as lookup_ops, math_ops as math_ops, nn as nn, string_ops as string_ops, weights_broadcast_ops as weights_broadcast_ops
from tensorflow.python.ops.losses import losses as losses
from tensorflow.python.saved_model import signature_constants as signature_constants
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import training_util as training_util
from tensorflow.python.util import function_utils as function_utils
from typing import Any as Any, Optional as Optional

LossSpec = namedtuple('LossSpec', ['training_loss', 'unreduced_loss', 'weights', 'processed_labels'])

class _Head(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    def name(self) -> Any: ...
    def logits_dimension(self) -> Any: ...
    @abc.abstractmethod
    def create_loss(self, features: Any, mode: Any, logits: Any, labels: Any) -> Any: ...
    def create_estimator_spec(self, features: Any, mode: Any, logits: Any, labels: Optional[Any] = ..., optimizer: Optional[Any] = ..., train_op_fn: Optional[Any] = ..., regularization_losses: Optional[Any] = ...): ...

class _MultiClassHeadWithSoftmaxCrossEntropyLoss(_Head):
    def __init__(self, n_classes: Any, weight_column: Optional[Any] = ..., label_vocabulary: Optional[Any] = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def logits_dimension(self): ...
    def create_loss(self, features: Any, mode: Any, logits: Any, labels: Any): ...

class _BinaryLogisticHeadWithSigmoidCrossEntropyLoss(_Head):
    def __init__(self, weight_column: Optional[Any] = ..., thresholds: Optional[Any] = ..., label_vocabulary: Optional[Any] = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def logits_dimension(self): ...
    def create_loss(self, features: Any, mode: Any, logits: Any, labels: Any): ...

class _RegressionHeadWithMeanSquaredErrorLoss(_Head):
    def __init__(self, label_dimension: Any, weight_column: Optional[Any] = ..., loss_reduction: Any = ..., loss_fn: Optional[Any] = ..., inverse_link_fn: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def logits_dimension(self): ...
    def create_loss(self, features: Any, mode: Any, logits: Any, labels: Any): ...
