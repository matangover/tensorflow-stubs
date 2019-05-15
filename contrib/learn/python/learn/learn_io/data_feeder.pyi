# Stubs for tensorflow.contrib.learn.python.learn.learn_io.data_feeder (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any as Any, Optional as Optional

def setup_train_data_feeder(x: Any, y: Any, n_classes: Any, batch_size: Optional[Any] = ..., shuffle: bool = ..., epochs: Optional[Any] = ...): ...
def setup_predict_data_feeder(x: Any, batch_size: Optional[Any] = ...): ...
def setup_processor_data_feeder(x: Any): ...
def check_array(array: Any, dtype: Any): ...

class DataFeeder:
    n_classes: Any = ...
    max_epochs: Any = ...
    random_state: Any = ...
    indices: Any = ...
    offset: int = ...
    epoch: int = ...
    def __init__(self, x: Any, y: Any, n_classes: Any, batch_size: Optional[Any] = ..., shuffle: bool = ..., random_state: Optional[Any] = ..., epochs: Optional[Any] = ...) -> None: ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def shuffle(self): ...
    @property
    def input_dtype(self): ...
    @property
    def output_dtype(self): ...
    @property
    def batch_size(self): ...
    def make_epoch_variable(self): ...
    def input_builder(self): ...
    def set_placeholders(self, input_placeholder: Any, output_placeholder: Any) -> None: ...
    def get_feed_params(self): ...
    def get_feed_dict_fn(self): ...

class StreamingDataFeeder(DataFeeder):
    n_classes: Any = ...
    def __init__(self, x: Any, y: Any, n_classes: Any, batch_size: Any) -> None: ...
    def get_feed_params(self): ...
    stopped: bool = ...
    def get_feed_dict_fn(self): ...

class DaskDataFeeder:
    df: Any = ...
    n_classes: Any = ...
    epochs: Any = ...
    sample_fraction: Any = ...
    random_state: int = ...
    def __init__(self, x: Any, y: Any, n_classes: Any, batch_size: Any, shuffle: bool = ..., random_state: Optional[Any] = ..., epochs: Optional[Any] = ...) -> None: ...
    def get_feed_params(self): ...
    def get_feed_dict_fn(self, input_placeholder: Any, output_placeholder: Any): ...
