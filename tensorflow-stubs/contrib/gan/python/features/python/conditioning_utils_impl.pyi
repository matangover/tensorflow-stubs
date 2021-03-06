# Stubs for tensorflow.contrib.gan.python.features.python.conditioning_utils_impl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.layers.python.layers import layers as layers
from tensorflow.python.framework import tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, embedding_ops as embedding_ops, math_ops as math_ops, variable_scope as variable_scope
from typing import Any as Any

def condition_tensor(tensor: Any, conditioning: Any): ...
def condition_tensor_from_onehot(tensor: Any, one_hot_labels: Any, embedding_size: int = ...): ...
