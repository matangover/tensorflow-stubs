# Stubs for tensorflow.contrib.specs.python.summaries (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.specs.python import specs as specs
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops
from typing import Any as Any, Optional as Optional

SHORT_NAMES_SRC: Any
SHORT_NAMES: Any

def tf_structure(x: Any, include_shapes: bool = ..., finished: Optional[Any] = ...): ...
def tf_print(x: Any, depth: int = ..., finished: Optional[Any] = ..., printer: Any = ...) -> None: ...
def tf_num_params(x: Any): ...
def tf_left_split(op: Any): ...
def tf_parameter_iter(x: Any) -> None: ...
def tf_parameter_summary(x: Any, printer: Any = ..., combine: bool = ...) -> None: ...
def tf_spec_structure(spec: Any, inputs: Optional[Any] = ..., input_shape: Optional[Any] = ..., input_type: Any = ...): ...
def tf_spec_summary(spec: Any, inputs: Optional[Any] = ..., input_shape: Optional[Any] = ..., input_type: Any = ...) -> None: ...
def tf_spec_print(spec: Any, inputs: Optional[Any] = ..., input_shape: Optional[Any] = ..., input_type: Any = ...) -> None: ...
