# Stubs for tensorflow.python.tools.inspect_checkpoint (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.platform import app as app, flags as flags
from typing import Any as Any

FLAGS: Any

def print_tensors_in_checkpoint_file(file_name: Any, tensor_name: Any, all_tensors: Any, all_tensor_names: bool = ...) -> None: ...
def parse_numpy_printoption(kv_str: Any) -> None: ...
def main(unused_argv: Any) -> None: ...