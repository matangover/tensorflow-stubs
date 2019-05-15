# Stubs for tensorflow.contrib.timeseries.python.timeseries.state_management (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.contrib.timeseries.python.timeseries import feature_keys as feature_keys, math_utils as math_utils
from tensorflow.contrib.timeseries.python.timeseries.model import ModelOutputs as ModelOutputs
from tensorflow.python.estimator import estimator_lib as estimator_lib
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

class PassthroughStateManager:
    def __init__(self) -> None: ...
    def initialize_graph(self, model: Any, input_statistics: Optional[Any] = ...) -> None: ...
    def define_loss(self, model: Any, features: Any, mode: Any): ...

class _OverridableStateManager(PassthroughStateManager, metaclass=abc.ABCMeta):
    def define_loss(self, model: Any, features: Any, mode: Any): ...

class FilteringOnlyStateManager(_OverridableStateManager): ...

class ChainingStateManager(_OverridableStateManager):
    def __init__(self, state_saving_interval: int = ..., checkpoint_state: bool = ...) -> None: ...
    def initialize_graph(self, model: Any, input_statistics: Optional[Any] = ...) -> None: ...
