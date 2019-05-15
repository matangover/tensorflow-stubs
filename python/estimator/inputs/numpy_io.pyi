# Stubs for tensorflow.python.estimator.inputs.numpy_io (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.estimator.inputs.queues import feeding_functions as feeding_functions
from tensorflow.python.util.tf_export import estimator_export as estimator_export
from typing import Any as Any, Optional as Optional

def numpy_input_fn(x: Any, y: Optional[Any] = ..., batch_size: int = ..., num_epochs: int = ..., shuffle: Optional[Any] = ..., queue_capacity: int = ..., num_threads: int = ...): ...
