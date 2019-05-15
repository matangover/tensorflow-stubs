# Stubs for tensorflow.contrib.lite.python.convert (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import enum as enum
from tensorflow.contrib.lite.python import lite_constants as lite_constants
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from typing import Any as Any, Optional as Optional

class ConverterMode(enum.Enum):
    DEFAULT: str = ...
    TOCO_FLEX: str = ...
    TOCO_FLEX_ALL: str = ...

def toco_convert_protos(model_flags_str: Any, toco_flags_str: Any, input_data_str: Any): ...
def tensor_name(x: Any): ...
def build_toco_convert_protos(input_tensors: Any, output_tensors: Any, inference_type: Any = ..., inference_input_type: Optional[Any] = ..., input_format: Any = ..., input_shapes: Optional[Any] = ..., output_format: Any = ..., quantized_input_stats: Optional[Any] = ..., default_ranges_stats: Optional[Any] = ..., drop_control_dependency: bool = ..., reorder_across_fake_quant: bool = ..., allow_custom_ops: bool = ..., change_concat_input_ranges: bool = ..., post_training_quantize: bool = ..., dump_graphviz_dir: Optional[Any] = ..., dump_graphviz_video: bool = ..., converter_mode: Any = ...): ...
def toco_convert_graph_def(input_data: Any, input_arrays_with_shape: Any, output_arrays: Any, *args: Any, **kwargs: Any): ...
def toco_convert_impl(input_data: Any, input_tensors: Any, output_tensors: Any, *args: Any, **kwargs: Any): ...
def toco_convert(input_data: Any, input_tensors: Any, output_tensors: Any, *args: Any, **kwargs: Any): ...