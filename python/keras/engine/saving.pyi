# Stubs for tensorflow.python.keras.engine.saving (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.keras import optimizers as optimizers
from tensorflow.python.keras.utils import conv_utils as conv_utils
from tensorflow.python.keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite
from tensorflow.python.util import serialization as serialization
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

HDF5_OBJECT_HEADER_LIMIT: int

def save_model(model: Any, filepath: Any, overwrite: bool = ..., include_optimizer: bool = ...) -> None: ...
def load_model(filepath: Any, custom_objects: Optional[Any] = ..., compile: bool = ...): ...
def model_from_config(config: Any, custom_objects: Optional[Any] = ...): ...
def model_from_yaml(yaml_string: Any, custom_objects: Optional[Any] = ...): ...
def model_from_json(json_string: Any, custom_objects: Optional[Any] = ...): ...
def preprocess_weights_for_loading(layer: Any, weights: Any, original_keras_version: Optional[Any] = ..., original_backend: Optional[Any] = ...): ...
def save_weights_to_hdf5_group(f: Any, layers: Any) -> None: ...
def load_weights_from_hdf5_group(f: Any, layers: Any) -> None: ...
def load_weights_from_hdf5_group_by_name(f: Any, layers: Any) -> None: ...
def save_attributes_to_hdf5_group(group: Any, name: Any, data: Any) -> None: ...
def load_attributes_from_hdf5_group(group: Any, name: Any): ...
