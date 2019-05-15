# Stubs for tensorflow.contrib.timeseries.python.timeseries.state_space_models.varma (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.timeseries.python.timeseries import math_utils as math_utils
from tensorflow.contrib.timeseries.python.timeseries.state_space_models import state_space_model as state_space_model
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, linalg_ops as linalg_ops, math_ops as math_ops, variable_scope as variable_scope
from typing import Any as Any

class VARMA(state_space_model.StateSpaceModel):
    ar_order: Any = ...
    ma_order: Any = ...
    state_num_blocks: Any = ...
    state_dimension: Any = ...
    def __init__(self, autoregressive_order: Any, moving_average_order: Any, configuration: Any = ...) -> None: ...
    def get_state_transition(self): ...
    def get_noise_transform(self): ...
    def get_observation_model(self, times: Any): ...
    def get_state_transition_noise_covariance(self, minimum_initial_variance: float = ...): ...