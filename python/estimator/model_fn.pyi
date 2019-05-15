# Stubs for tensorflow.python.estimator.model_fn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.keras.metrics import Metric as Metric
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.saved_model import signature_constants as signature_constants, tag_constants as tag_constants
from tensorflow.python.training import monitored_session as monitored_session, session_run_hook as session_run_hook
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import estimator_export as estimator_export
from typing import Any as Any, Optional as Optional

class ModeKeys:
    TRAIN: str = ...
    EVAL: str = ...
    PREDICT: str = ...

LOSS_METRIC_KEY: str
AVERAGE_LOSS_METRIC_KEY: str
EXPORT_TAG_MAP: Any

class EstimatorSpec:
    def __new__(cls, mode: Any, predictions: Optional[Any] = ..., loss: Optional[Any] = ..., train_op: Optional[Any] = ..., eval_metric_ops: Optional[Any] = ..., export_outputs: Optional[Any] = ..., training_chief_hooks: Optional[Any] = ..., training_hooks: Optional[Any] = ..., scaffold: Optional[Any] = ..., evaluation_hooks: Optional[Any] = ..., prediction_hooks: Optional[Any] = ...): ...

class _TPUEstimatorSpec:
    def __new__(cls, mode: Any, predictions: Optional[Any] = ..., loss: Optional[Any] = ..., train_op: Optional[Any] = ..., eval_metrics: Optional[Any] = ..., export_outputs: Optional[Any] = ..., scaffold_fn: Optional[Any] = ..., host_call: Optional[Any] = ..., training_hooks: Optional[Any] = ..., evaluation_hooks: Optional[Any] = ..., prediction_hooks: Optional[Any] = ...): ...
    def as_estimator_spec(self): ...

def export_outputs_for_mode(mode: Any, serving_export_outputs: Optional[Any] = ..., predictions: Optional[Any] = ..., loss: Optional[Any] = ..., metrics: Optional[Any] = ...): ...
