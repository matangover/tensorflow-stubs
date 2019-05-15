# Stubs for tensorflow.contrib.specs.python.specs (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.specs.python import params_ops as params_ops, specs_lib as specs_lib, specs_ops as specs_ops
from tensorflow.python.util import tf_inspect as tf_inspect
from typing import Any as Any, Optional as Optional

def eval_params(params: Any, environment: Optional[Any] = ...): ...
def eval_spec(spec: Any, environment: Optional[Any] = ...): ...
def create_net_fun(spec: Any, environment: Optional[Any] = ...): ...
def create_net(spec: Any, inputs: Any, environment: Optional[Any] = ...): ...

class LocalImport:
    names: Any = ...
    def __init__(self, names: Any) -> None: ...
    frame: Any = ...
    old: Any = ...
    def __enter__(self) -> None: ...
    def __exit__(self, some_type: Any, value: Any, traceback: Any) -> None: ...

ops: Any
