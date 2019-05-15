# Stubs for tensorflow.python.keras.utils.multi_gpu_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.keras.engine.training import Model as Model
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

def multi_gpu_model(model: Any, gpus: Any, cpu_merge: bool = ..., cpu_relocation: bool = ...): ...
