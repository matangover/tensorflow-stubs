# Stubs for tensorflow.contrib.predictor.core_estimator_predictor (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.predictor import predictor as predictor
from tensorflow.python.estimator import model_fn as model_fn
from tensorflow.python.framework import ops as ops
from tensorflow.python.saved_model import signature_constants as signature_constants
from tensorflow.python.training import monitored_session as monitored_session
from typing import Any as Any, Optional as Optional

class CoreEstimatorPredictor(predictor.Predictor):
    def __init__(self, estimator: Any, serving_input_receiver_fn: Any, output_key: Optional[Any] = ..., graph: Optional[Any] = ..., config: Optional[Any] = ...) -> None: ...