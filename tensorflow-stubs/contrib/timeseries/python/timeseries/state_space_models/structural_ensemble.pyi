# Stubs for tensorflow.contrib.timeseries.python.timeseries.state_space_models.structural_ensemble (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.timeseries.python.timeseries.state_space_models import level_trend as level_trend, periodic as periodic, state_space_model as state_space_model, varma as varma
from tensorflow.python.ops import variable_scope as variable_scope
from tensorflow.python.util import nest as nest
from typing import Any as Any

class StructuralEnsemble(state_space_model.StateSpaceIndependentEnsemble):
    def __init__(self, periodicities: Any, moving_average_order: Any, autoregressive_order: Any, use_level_noise: bool = ..., configuration: Any = ...) -> None: ...

class MultiResolutionStructuralEnsemble(state_space_model.StateSpaceIndependentEnsemble):
    def __init__(self, cycle_num_latent_values: Any, moving_average_order: Any, autoregressive_order: Any, periodicities: Any, use_level_noise: bool = ..., configuration: Any = ...) -> None: ...
