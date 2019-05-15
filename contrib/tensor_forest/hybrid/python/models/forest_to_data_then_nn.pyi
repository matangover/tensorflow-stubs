# Stubs for tensorflow.contrib.tensor_forest.hybrid.python.models.forest_to_data_then_nn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.tensor_forest.hybrid.python import hybrid_model as hybrid_model
from tensorflow.contrib.tensor_forest.hybrid.python.layers import decisions_to_data as decisions_to_data, fully_connected as fully_connected
from tensorflow.python.training import adagrad as adagrad
from typing import Any as Any, Optional as Optional

class ForestToDataThenNN(hybrid_model.HybridModel):
    layers: Any = ...
    def __init__(self, params: Any, device_assigner: Optional[Any] = ..., optimizer_class: Any = ..., **kwargs: Any) -> None: ...
