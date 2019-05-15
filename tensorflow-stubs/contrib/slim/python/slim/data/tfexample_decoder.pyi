# Stubs for tensorflow.contrib.slim.python.slim.data.tfexample_decoder (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.contrib.slim.python.slim.data import data_decoder as data_decoder
from tensorflow.python.framework import dtypes as dtypes, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, functional_ops as functional_ops, image_ops as image_ops, math_ops as math_ops, parsing_ops as parsing_ops, sparse_ops as sparse_ops
from typing import Any as Any, Optional as Optional

class ItemHandler(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    def __init__(self, keys: Any) -> None: ...
    @property
    def keys(self): ...
    @abc.abstractmethod
    def tensors_to_item(self, keys_to_tensors: Any) -> Any: ...

class ItemHandlerCallback(ItemHandler):
    def __init__(self, keys: Any, func: Any) -> None: ...
    def tensors_to_item(self, keys_to_tensors: Any): ...

class BoundingBox(ItemHandler):
    def __init__(self, keys: Optional[Any] = ..., prefix: str = ...) -> None: ...
    def tensors_to_item(self, keys_to_tensors: Any): ...

class Tensor(ItemHandler):
    def __init__(self, tensor_key: Any, shape_keys: Optional[Any] = ..., shape: Optional[Any] = ..., default_value: int = ...) -> None: ...
    def tensors_to_item(self, keys_to_tensors: Any): ...

class LookupTensor(Tensor):
    def __init__(self, tensor_key: Any, table: Any, shape_keys: Optional[Any] = ..., shape: Optional[Any] = ..., default_value: str = ...) -> None: ...
    def tensors_to_item(self, keys_to_tensors: Any): ...

class BackupHandler(ItemHandler):
    def __init__(self, handler: Any, backup: Any) -> None: ...
    def tensors_to_item(self, keys_to_tensors: Any): ...

class SparseTensor(ItemHandler):
    def __init__(self, indices_key: Optional[Any] = ..., values_key: Optional[Any] = ..., shape_key: Optional[Any] = ..., shape: Optional[Any] = ..., densify: bool = ..., default_value: int = ...) -> None: ...
    def tensors_to_item(self, keys_to_tensors: Any): ...

class Image(ItemHandler):
    def __init__(self, image_key: Optional[Any] = ..., format_key: Optional[Any] = ..., shape: Optional[Any] = ..., channels: int = ..., dtype: Any = ..., repeated: bool = ..., dct_method: str = ...) -> None: ...
    def tensors_to_item(self, keys_to_tensors: Any): ...

class TFExampleDecoder(data_decoder.DataDecoder):
    def __init__(self, keys_to_features: Any, items_to_handlers: Any) -> None: ...
    def list_items(self): ...
    def decode(self, serialized_example: Any, items: Optional[Any] = ...): ...