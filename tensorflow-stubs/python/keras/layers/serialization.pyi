# Stubs for tensorflow.python.keras.layers.serialization (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.keras.layers.advanced_activations import *
from tensorflow.python.keras.layers.convolutional import *
from tensorflow.python.keras.layers.convolutional_recurrent import *
from tensorflow.python.keras.layers.core import *
from tensorflow.python.keras.layers.cudnn_recurrent import *
from tensorflow.python.keras.layers.embeddings import *
from tensorflow.python.keras.layers.local import *
from tensorflow.python.keras.layers.merge import *
from tensorflow.python.keras.layers.noise import *
from tensorflow.python.keras.layers.normalization import *
from tensorflow.python.keras.layers.pooling import *
from tensorflow.python.keras.layers.recurrent import *
from tensorflow.python.keras.layers.wrappers import *
from tensorflow.python.keras.engine.input_layer import Input as Input, InputLayer as InputLayer
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object
from typing import Any as Any, Optional as Optional

def serialize(layer: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...