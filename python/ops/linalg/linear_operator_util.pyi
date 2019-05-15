# Stubs for tensorflow.python.ops.linalg.linear_operator_util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, linalg_ops as linalg_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

def assert_no_entries_with_modulus_zero(x: Any, message: Optional[Any] = ..., name: str = ...): ...
def assert_zero_imag_part(x: Any, message: Optional[Any] = ..., name: str = ...): ...
def assert_compatible_matrix_dimensions(operator: Any, x: Any): ...
def assert_is_batch_matrix(tensor: Any) -> None: ...
def shape_tensor(shape: Any, name: Optional[Any] = ...): ...
def broadcast_matrix_batch_dims(batch_matrices: Any, name: Optional[Any] = ...): ...
def cholesky_solve_with_broadcast(chol: Any, rhs: Any, name: Optional[Any] = ...): ...
def matmul_with_broadcast(a: Any, b: Any, transpose_a: bool = ..., transpose_b: bool = ..., adjoint_a: bool = ..., adjoint_b: bool = ..., a_is_sparse: bool = ..., b_is_sparse: bool = ..., name: Optional[Any] = ...): ...
def matrix_solve_with_broadcast(matrix: Any, rhs: Any, adjoint: bool = ..., name: Optional[Any] = ...): ...
def matrix_triangular_solve_with_broadcast(matrix: Any, rhs: Any, lower: bool = ..., adjoint: bool = ..., name: Optional[Any] = ...): ...