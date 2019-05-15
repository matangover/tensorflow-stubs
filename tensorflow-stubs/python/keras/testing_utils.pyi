# Stubs for tensorflow.python.keras.testing_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python import keras as keras
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.training.rmsprop import RMSPropOptimizer as RMSPropOptimizer
from tensorflow.python.util import tf_inspect as tf_inspect
from typing import Any as Any, Optional as Optional

def get_test_data(train_samples: Any, test_samples: Any, input_shape: Any, num_classes: Any, random_seed: Optional[Any] = ...): ...
def layer_test(layer_cls: Any, kwargs: Optional[Any] = ..., input_shape: Optional[Any] = ..., input_dtype: Optional[Any] = ..., input_data: Optional[Any] = ..., expected_output: Optional[Any] = ..., expected_output_dtype: Optional[Any] = ...): ...
def get_small_sequential_mlp(num_hidden: Any, num_classes: Any, input_dim: Optional[Any] = ...): ...
def get_small_functional_mlp(num_hidden: Any, num_classes: Any, input_dim: Any): ...