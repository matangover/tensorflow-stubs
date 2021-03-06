# Stubs for tensorflow.contrib.eager.python.metrics_impl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, variable_scope as variable_scope
from tensorflow.python.training.checkpointable import base as checkpointable
from typing import Any as Any, Optional as Optional

class Metric(checkpointable.CheckpointableBase):
    build: Any = ...
    call: Any = ...
    def __init__(self, name: Optional[Any] = ..., use_global_variables: bool = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    @property
    def name(self): ...
    @property
    def variables(self): ...
    def init_variables(self): ...
    def build(self, *args: Any, **kwargs: Any) -> None: ...
    def call(self, *args: Any, **kwargs: Any) -> None: ...
    def result(self) -> None: ...
    def value(self): ...
    def aggregate(self, metrics: Any) -> None: ...
    def add_variable(self, name: Any, shape: Optional[Any] = ..., dtype: Optional[Any] = ..., initializer: Optional[Any] = ...): ...

class Mean(Metric):
    dtype: Any = ...
    def __init__(self, name: Optional[Any] = ..., dtype: Any = ..., use_global_variables: bool = ...) -> None: ...
    numer: Any = ...
    denom: Any = ...
    def build(self, *args: Any, **kwargs: Any) -> None: ...
    def call(self, values: Any, weights: Optional[Any] = ...): ...
    def result(self, write_summary: bool = ...): ...

class Accuracy(Mean):
    def __init__(self, name: Optional[Any] = ..., dtype: Any = ...) -> None: ...
    def call(self, labels: Any, predictions: Any, weights: Optional[Any] = ...): ...

class CategoricalAccuracy(Mean):
    def __init__(self, name: Optional[Any] = ..., dtype: Any = ...) -> None: ...
    def call(self, labels: Any, predictions: Any, weights: Optional[Any] = ...): ...

class BinaryAccuracy(Mean):
    threshold: Any = ...
    def __init__(self, threshold: Any, name: Optional[Any] = ..., dtype: Any = ...) -> None: ...
    def call(self, labels: Any, predictions: Any, weights: Optional[Any] = ...): ...

class SparseAccuracy(Mean):
    def __init__(self, name: Optional[Any] = ..., dtype: Any = ...) -> None: ...
    def call(self, labels: Any, predictions: Any, weights: Optional[Any] = ...): ...
