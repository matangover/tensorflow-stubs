# Stubs for tensorflow.python.keras.engine.base_layer (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import enum as enum
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.utils import generic_utils as generic_utils, tf_utils as tf_utils
from tensorflow.python.keras.utils.generic_utils import to_snake_case as to_snake_case
from tensorflow.python.keras.utils.tf_utils import is_tensor_or_tensor_list as is_tensor_or_tensor_list
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops
from tensorflow.python.training.checkpointable import base as checkpointable
from tensorflow.python.util import function_utils as function_utils, nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any as Any, Optional as Optional

class CallConvention(enum.Enum):
    EXPLICIT_INPUTS_ARGUMENT: int = ...
    SINGLE_POSITIONAL_ARGUMENT: int = ...
    POSITIONAL_ARGUMENTS_ARE_INPUTS: int = ...

class Layer(checkpointable.CheckpointableBase):
    trainable: Any = ...
    stateful: bool = ...
    built: bool = ...
    input_spec: Any = ...
    supports_masking: bool = ...
    def __init__(self, trainable: bool = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def dtype(self): ...
    @property
    def name(self): ...
    @property
    def activity_regularizer(self): ...
    @activity_regularizer.setter
    def activity_regularizer(self, regularizer: Any) -> None: ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def weights(self): ...
    @property
    def variables(self): ...
    @property
    def updates(self): ...
    def add_update(self, updates: Any, inputs: Optional[Any] = ...): ...
    def get_updates_for(self, inputs: Any): ...
    @property
    def losses(self): ...
    def add_loss(self, losses: Any, inputs: Optional[Any] = ...): ...
    def get_losses_for(self, inputs: Any): ...
    def build(self, input_shape: Any) -> None: ...
    def add_variable(self, *args: Any, **kwargs: Any): ...
    def add_weight(self, name: Any, shape: Any, dtype: Optional[Any] = ..., initializer: Optional[Any] = ..., regularizer: Optional[Any] = ..., trainable: Optional[Any] = ..., constraint: Optional[Any] = ..., partitioner: Optional[Any] = ..., use_resource: Optional[Any] = ..., synchronization: Any = ..., aggregation: Any = ..., **kwargs: Any): ...
    def call(self, inputs: Any, **kwargs: Any): ...
    def __call__(self, inputs: Any, *args: Any, **kwargs: Any): ...
    def apply(self, inputs: Any, *args: Any, **kwargs: Any): ...
    def compute_output_shape(self, input_shape: Any): ...
    def compute_mask(self, inputs: Any, mask: Optional[Any] = ...): ...
    def get_input_mask_at(self, node_index: Any): ...
    def get_output_mask_at(self, node_index: Any): ...
    @property
    def input_mask(self): ...
    @property
    def output_mask(self): ...
    def get_input_shape_at(self, node_index: Any): ...
    def get_output_shape_at(self, node_index: Any): ...
    def get_input_at(self, node_index: Any): ...
    def get_output_at(self, node_index: Any): ...
    @property
    def input(self): ...
    @property
    def output(self): ...
    @property
    def input_shape(self): ...
    def count_params(self): ...
    @property
    def output_shape(self): ...
    @property
    def inbound_nodes(self): ...
    @property
    def outbound_nodes(self): ...
    def set_weights(self, weights: Any) -> None: ...
    def get_weights(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any): ...

class InputSpec:
    dtype: Any = ...
    shape: Any = ...
    ndim: Any = ...
    max_ndim: Any = ...
    min_ndim: Any = ...
    axes: Any = ...
    def __init__(self, dtype: Optional[Any] = ..., shape: Optional[Any] = ..., ndim: Optional[Any] = ..., max_ndim: Optional[Any] = ..., min_ndim: Optional[Any] = ..., axes: Optional[Any] = ...) -> None: ...

class Node:
    outbound_layer: Any = ...
    inbound_layers: Any = ...
    node_indices: Any = ...
    tensor_indices: Any = ...
    input_tensors: Any = ...
    output_tensors: Any = ...
    input_shapes: Any = ...
    output_shapes: Any = ...
    arguments: Any = ...
    def __init__(self, outbound_layer: Any, inbound_layers: Any, node_indices: Any, tensor_indices: Any, input_tensors: Any, output_tensors: Any, arguments: Optional[Any] = ...) -> None: ...
    def get_config(self): ...

class DeferredTensor:
    shape: Any = ...
    dtype: Any = ...
    name: Any = ...
    def __init__(self, shape: Any, dtype: Any, name: Optional[Any] = ...) -> None: ...
    def get_shape(self): ...

def unique_layer_name(name: Any, name_uid_map: Optional[Any] = ..., avoid_names: Optional[Any] = ..., namespace: str = ..., zero_based: bool = ...): ...
def have_all_keras_metadata(iterable_or_element: Any): ...
def collect_previous_mask(input_tensors: Any): ...
def get_default_graph_uid_map(): ...
def make_variable(name: Any, shape: Optional[Any] = ..., dtype: Any = ..., initializer: Optional[Any] = ..., partition_info: Optional[Any] = ..., trainable: Optional[Any] = ..., caching_device: Optional[Any] = ..., validate_shape: bool = ..., constraint: Optional[Any] = ..., use_resource: Optional[Any] = ..., collections: Optional[Any] = ..., synchronization: Any = ..., aggregation: Any = ..., partitioner: Optional[Any] = ...): ...
def default(method: Any): ...
def generate_placeholders_from_shape(shape: Any): ...