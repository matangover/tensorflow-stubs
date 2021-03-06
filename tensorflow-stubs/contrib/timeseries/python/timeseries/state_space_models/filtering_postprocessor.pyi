# Stubs for tensorflow.contrib.timeseries.python.timeseries.state_space_models.filtering_postprocessor (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.contrib import distributions as distributions
from tensorflow.contrib.timeseries.python.timeseries import math_utils as math_utils
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.util import nest as nest
from typing import Any as Any

class FilteringStepPostprocessor(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    @abc.abstractmethod
    def process_filtering_step(self, current_times: Any, current_values: Any, predicted_state: Any, filtered_state: Any, outputs: Any) -> Any: ...
    def output_names(self) -> Any: ...

def cauchy_alternative_to_gaussian(current_times: Any, current_values: Any, outputs: Any): ...

class StateInterpolatingAnomalyDetector(FilteringStepPostprocessor):
    output_names: Any = ...
    def __init__(self, anomaly_log_likelihood: Any = ..., anomaly_prior_probability: float = ..., responsibility_scaling: float = ...) -> None: ...
    def process_filtering_step(self, current_times: Any, current_values: Any, predicted_state: Any, filtered_state: Any, outputs: Any): ...
