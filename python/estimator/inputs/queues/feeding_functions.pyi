# Stubs for tensorflow.python.estimator.inputs.queues.feeding_functions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, errors as errors, ops as ops
from tensorflow.python.ops import array_ops as array_ops, data_flow_ops as data_flow_ops, math_ops as math_ops
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import queue_runner as queue_runner
from typing import Any as Any, Optional as Optional

HAS_PANDAS: bool

class _ArrayFeedFn:
    def __init__(self, placeholders: Any, array: Any, batch_size: Any, random_start: bool = ..., seed: Optional[Any] = ..., num_epochs: Optional[Any] = ...) -> None: ...
    def __call__(self): ...

class _OrderedDictNumpyFeedFn:
    def __init__(self, placeholders: Any, ordered_dict_of_arrays: Any, batch_size: Any, random_start: bool = ..., seed: Optional[Any] = ..., num_epochs: Optional[Any] = ...) -> None: ...
    def __call__(self): ...

class _PandasFeedFn:
    def __init__(self, placeholders: Any, dataframe: Any, batch_size: Any, random_start: bool = ..., seed: Optional[Any] = ..., num_epochs: Optional[Any] = ...) -> None: ...
    def __call__(self): ...

class _GeneratorFeedFn:
    def __init__(self, placeholders: Any, generator: Any, batch_size: Any, random_start: bool = ..., seed: Optional[Any] = ..., num_epochs: Optional[Any] = ..., pad_value: Optional[Any] = ...) -> None: ...
    def __call__(self): ...
