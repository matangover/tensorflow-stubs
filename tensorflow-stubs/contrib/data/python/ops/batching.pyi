# Stubs for tensorflow.contrib.data.python.ops.batching (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.framework import with_shape as with_shape
from tensorflow.python.data.experimental.ops import batching as batching
from tensorflow.python.data.util import nest as nest
from tensorflow.python.util import deprecation as deprecation
from typing import Any as Any, Optional as Optional

def dense_to_sparse_batch(batch_size: Any, row_shape: Any): ...
def unbatch(): ...
def batch_and_drop_remainder(batch_size: Any): ...
def padded_batch_and_drop_remainder(batch_size: Any, padded_shapes: Any, padding_values: Optional[Any] = ...): ...
def assert_element_shape(expected_shapes: Any): ...
def map_and_batch(map_func: Any, batch_size: Any, num_parallel_batches: Optional[Any] = ..., drop_remainder: bool = ..., num_parallel_calls: Optional[Any] = ...): ...
