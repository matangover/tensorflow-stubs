# Stubs for tensorflow.python.ops.distributions.bijector_test_util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import math_ops as math_ops
from typing import Any as Any, Optional as Optional

def assert_finite(array: Any) -> None: ...
def assert_strictly_increasing(array: Any) -> None: ...
def assert_strictly_decreasing(array: Any) -> None: ...
def assert_strictly_monotonic(array: Any) -> None: ...
def assert_scalar_congruency(bijector: Any, lower_x: Any, upper_x: Any, n: Any = ..., rtol: float = ..., sess: Optional[Any] = ...) -> None: ...
def assert_bijective_and_finite(bijector: Any, x: Any, y: Any, event_ndims: Any, atol: int = ..., rtol: float = ..., sess: Optional[Any] = ...) -> None: ...