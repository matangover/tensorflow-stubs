# Stubs for tensorflow.python.framework.error_interpolation (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util import tf_stack as tf_stack
from typing import Any as Any

_ParseTag = namedtuple('_ParseTag', ['type', 'name'])

def compute_field_dict(op: Any): ...
def interpolate(error_message: Any, graph: Any): ...