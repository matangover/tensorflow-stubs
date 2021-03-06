# Stubs for tensorflow.contrib.factorization.python.ops.factorization_ops_test_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import constant_op as constant_op, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, sparse_ops as sparse_ops
from typing import Any as Any, Optional as Optional

INPUT_MATRIX: Any

def remove_empty_rows_columns(np_matrix: Any): ...
def np_matrix_to_tf_sparse(np_matrix: Any, row_slices: Optional[Any] = ..., col_slices: Optional[Any] = ..., transpose: bool = ..., shuffle: bool = ...): ...
def calculate_loss(input_mat: Any, row_factors: Any, col_factors: Any, regularization: Optional[Any] = ..., w0: float = ..., row_weights: Optional[Any] = ..., col_weights: Optional[Any] = ...): ...
