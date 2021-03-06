# Stubs for tensorflow.python.ops.linalg.linear_operator (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, linalg_ops as linalg_ops, math_ops as math_ops
from tensorflow.python.ops.linalg import linear_operator_util as linear_operator_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class LinearOperator(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    def __init__(self, dtype: Any, graph_parents: Optional[Any] = ..., is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def dtype(self): ...
    @property
    def name(self): ...
    @property
    def graph_parents(self): ...
    @property
    def is_non_singular(self): ...
    @property
    def is_self_adjoint(self): ...
    @property
    def is_positive_definite(self): ...
    @property
    def is_square(self): ...
    @property
    def shape(self): ...
    def shape_tensor(self, name: str = ...): ...
    @property
    def batch_shape(self): ...
    def batch_shape_tensor(self, name: str = ...): ...
    @property
    def tensor_rank(self, name: str = ...): ...
    def tensor_rank_tensor(self, name: str = ...): ...
    @property
    def domain_dimension(self): ...
    def domain_dimension_tensor(self, name: str = ...): ...
    @property
    def range_dimension(self): ...
    def range_dimension_tensor(self, name: str = ...): ...
    def assert_non_singular(self, name: str = ...): ...
    def assert_positive_definite(self, name: str = ...): ...
    def assert_self_adjoint(self, name: str = ...): ...
    def matmul(self, x: Any, adjoint: bool = ..., adjoint_arg: bool = ..., name: str = ...): ...
    def matvec(self, x: Any, adjoint: bool = ..., name: str = ...): ...
    def determinant(self, name: str = ...): ...
    def log_abs_determinant(self, name: str = ...): ...
    def solve(self, rhs: Any, adjoint: bool = ..., adjoint_arg: bool = ..., name: str = ...): ...
    def solvevec(self, rhs: Any, adjoint: bool = ..., name: str = ...): ...
    def to_dense(self, name: str = ...): ...
    def diag_part(self, name: str = ...): ...
    def trace(self, name: str = ...): ...
    def add_to_tensor(self, x: Any, name: str = ...): ...
