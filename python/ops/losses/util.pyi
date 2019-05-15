# Stubs for tensorflow.python.ops.losses.util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def add_loss(loss: Any, loss_collection: Any = ...) -> None: ...
def get_losses(scope: Optional[Any] = ..., loss_collection: Any = ...): ...
def get_regularization_losses(scope: Optional[Any] = ...): ...
def get_regularization_loss(scope: Optional[Any] = ..., name: str = ...): ...
def get_total_loss(add_regularization_losses: bool = ..., name: str = ...): ...