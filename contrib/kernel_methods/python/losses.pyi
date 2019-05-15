# Stubs for tensorflow.contrib.kernel_methods.python.losses (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, nn_ops as nn_ops
from tensorflow.python.ops.losses import losses as losses
from typing import Any as Any, Optional as Optional

def sparse_multiclass_hinge_loss(labels: Any, logits: Any, weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...