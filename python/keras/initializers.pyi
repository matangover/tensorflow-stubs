# Stubs for tensorflow.python.keras.initializers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from tensorflow.python.ops.init_ops import Constant as Constant, GlorotNormal as GlorotNormal, GlorotUniform as GlorotUniform, Identity as Identity, Initializer as Initializer, Ones as Ones, Orthogonal as Orthogonal, RandomNormal as TFRandomNormal, RandomUniform as TFRandomUniform, TruncatedNormal as TFTruncatedNormal, VarianceScaling as VarianceScaling, Zeros as Zeros, he_normal as he_normal, he_uniform as he_uniform, lecun_normal as lecun_normal, lecun_uniform as lecun_uniform
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class TruncatedNormal(TFTruncatedNormal):
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Optional[Any] = ..., dtype: Any = ...) -> None: ...

class RandomUniform(TFRandomUniform):
    def __init__(self, minval: Any = ..., maxval: float = ..., seed: Optional[Any] = ..., dtype: Any = ...) -> None: ...

class RandomNormal(TFRandomNormal):
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Optional[Any] = ..., dtype: Any = ...) -> None: ...
zero = Zeros
zeros = Zeros
one = Ones
ones = Ones
constant = Constant
uniform = RandomUniform
random_uniform = RandomUniform
normal = RandomNormal
random_normal = RandomNormal
truncated_normal = TruncatedNormal
identity = Identity
orthogonal = Orthogonal
glorot_normal = GlorotNormal
glorot_uniform = GlorotUniform

def serialize(initializer: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...
def get(identifier: Any): ...
