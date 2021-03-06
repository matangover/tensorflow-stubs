# Stubs for tensorflow.python.ops.linalg.linear_operator_circulant (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.ops.linalg import linear_operator as linear_operator, linear_operator_util as linear_operator_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class _BaseLinearOperatorCirculant(linear_operator.LinearOperator):
    def __init__(self, spectrum: Any, block_depth: Any, input_output_dtype: Any = ..., is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: bool = ..., name: str = ...) -> None: ...
    @property
    def block_depth(self): ...
    def block_shape_tensor(self): ...
    @property
    def block_shape(self): ...
    @property
    def spectrum(self): ...
    def convolution_kernel(self, name: str = ...): ...
    def assert_hermitian_spectrum(self, name: str = ...): ...

class LinearOperatorCirculant(_BaseLinearOperatorCirculant):
    def __init__(self, spectrum: Any, input_output_dtype: Any = ..., is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: bool = ..., name: str = ...) -> None: ...

class LinearOperatorCirculant2D(_BaseLinearOperatorCirculant):
    def __init__(self, spectrum: Any, input_output_dtype: Any = ..., is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: bool = ..., name: str = ...) -> None: ...

class LinearOperatorCirculant3D(_BaseLinearOperatorCirculant):
    def __init__(self, spectrum: Any, input_output_dtype: Any = ..., is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: bool = ..., name: str = ...) -> None: ...
