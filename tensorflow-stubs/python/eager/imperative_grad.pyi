# Stubs for tensorflow.python.eager.imperative_grad (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from typing import Any as Any, Optional as Optional

VSpace = namedtuple('VSpace', ['aggregate_fn', 'num_elements_fn', 'zeros_fn', 'ones_fn', 'graph_shape_fn'])

def imperative_grad(tape: Any, target: Any, sources: Any, output_gradients: Optional[Any] = ...): ...