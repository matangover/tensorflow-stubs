# Stubs for tensorflow.python.ops.linalg.linear_operator_diag (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.ops.linalg import linear_operator as linear_operator, linear_operator_util as linear_operator_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class LinearOperatorDiag(linear_operator.LinearOperator):
    def __init__(self, diag: Any, is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: Optional[Any] = ..., name: str = ...) -> None: ...
    @property
    def diag(self): ...