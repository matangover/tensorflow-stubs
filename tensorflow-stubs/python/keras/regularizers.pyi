# Stubs for tensorflow.python.keras.regularizers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class Regularizer:
    def __call__(self, x: Any): ...
    @classmethod
    def from_config(cls, config: Any): ...

class L1L2(Regularizer):
    l1: Any = ...
    l2: Any = ...
    def __init__(self, l1: float = ..., l2: float = ...) -> None: ...
    def __call__(self, x: Any): ...
    def get_config(self): ...

def l1(l: float = ...): ...
def l2(l: float = ...): ...
def l1_l2(l1: float = ..., l2: float = ...): ...
def serialize(regularizer: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...
def get(identifier: Any): ...
