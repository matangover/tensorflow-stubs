# Stubs for tensorflow.python.keras.engine.training_distributed (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, errors as errors, tensor_shape as tensor_shape
from tensorflow.python.keras import optimizers as optimizers
from tensorflow.python.keras.engine import distributed_training_utils as distributed_training_utils
from tensorflow.python.keras.utils.generic_utils import Progbar as Progbar
from tensorflow.python.ops import array_ops as array_ops, variable_scope as variable_scope
from typing import Any as Any, Optional as Optional

def fit_loop(model: Any, iterator: Any, epochs: int = ..., verbose: int = ..., callbacks: Optional[Any] = ..., val_iterator: Optional[Any] = ..., initial_epoch: int = ..., steps_per_epoch: Optional[Any] = ..., validation_steps: Optional[Any] = ...): ...
def test_loop(model: Any, iterator: Any, verbose: int = ..., steps: Optional[Any] = ...): ...
def predict_loop(model: Any, iterator: Any, verbose: int = ..., steps: Optional[Any] = ...): ...
def clone_model_on_towers(model: Any, strategy: Any, make_callback_model: bool = ..., inputs: Optional[Any] = ..., targets: Optional[Any] = ...) -> None: ...