# Stubs for tensorflow.contrib.learn.python.learn.datasets.mnist (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.learn.python.learn.datasets import base as base
from tensorflow.python.framework import dtypes as dtypes, random_seed as random_seed
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any as Any, Optional as Optional

DEFAULT_SOURCE_URL: str

def extract_images(f: Any): ...
def dense_to_one_hot(labels_dense: Any, num_classes: Any): ...
def extract_labels(f: Any, one_hot: bool = ..., num_classes: int = ...): ...

class DataSet:
    one_hot: Any = ...
    def __init__(self, images: Any, labels: Any, fake_data: bool = ..., one_hot: bool = ..., dtype: Any = ..., reshape: bool = ..., seed: Optional[Any] = ...) -> None: ...
    @property
    def images(self): ...
    @property
    def labels(self): ...
    @property
    def num_examples(self): ...
    @property
    def epochs_completed(self): ...
    def next_batch(self, batch_size: Any, fake_data: bool = ..., shuffle: bool = ...): ...

def read_data_sets(train_dir: Any, fake_data: bool = ..., one_hot: bool = ..., dtype: Any = ..., reshape: bool = ..., validation_size: int = ..., seed: Optional[Any] = ..., source_url: Any = ...): ...
def load_mnist(train_dir: str = ...): ...