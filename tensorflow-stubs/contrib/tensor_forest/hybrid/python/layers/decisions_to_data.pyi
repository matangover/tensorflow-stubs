# Stubs for tensorflow.contrib.tensor_forest.hybrid.python.layers.decisions_to_data (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.tensor_forest.hybrid.ops import gen_training_ops as gen_training_ops
from tensorflow.contrib.tensor_forest.hybrid.python import hybrid_layer as hybrid_layer
from tensorflow.contrib.tensor_forest.hybrid.python.ops import training_ops as training_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, variable_scope as variable_scope
from typing import Any as Any

class DecisionsToDataLayer(hybrid_layer.HybridLayer):
    def __init__(self, params: Any, layer_num: Any, device_assigner: Any, *args: Any, **kwargs: Any) -> None: ...
    def inference_graph(self, data: Any): ...

class KFeatureDecisionsToDataLayer(hybrid_layer.HybridLayer):
    def __init__(self, params: Any, layer_num: Any, device_assigner: Any, *args: Any, **kwargs: Any) -> None: ...
    def inference_graph(self, data: Any): ...

class HardDecisionsToDataLayer(DecisionsToDataLayer):
    def soft_inference_graph(self, data: Any): ...
    def inference_graph(self, data: Any): ...

class StochasticHardDecisionsToDataLayer(HardDecisionsToDataLayer):
    def soft_inference_graph(self, data: Any): ...
    def inference_graph(self, data: Any): ...

class StochasticSoftDecisionsToDataLayer(StochasticHardDecisionsToDataLayer):
    def inference_graph(self, data: Any): ...
