# Stubs for tensorflow.contrib.tensor_forest.hybrid.python.hybrid_layer (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any, Optional as Optional

class HybridLayer:
    layer_num: Any = ...
    device_assigner: Any = ...
    params: Any = ...
    def __init__(self, params: Any, layer_num: Any, device_assigner: Any, *args: Any, **kwargs: Any) -> None: ...
    def inference_graph(self, data: Any, data_spec: Optional[Any] = ...) -> None: ...
