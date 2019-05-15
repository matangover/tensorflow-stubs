# Stubs for tensorflow.contrib.eager.python.parameter_server (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops, variable_scope as variable_scope
from typing import Any as Any, Optional as Optional

class SharedVariable(resource_variable_ops.ResourceVariable):
    def __init__(self, initial_value: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., constraint: Optional[Any] = ..., initialize: bool = ..., **unused_kwargs: Any) -> None: ...

def parameter_server_scope(is_chief: Any, ps_job_name: Any, num_ps_tasks: Any): ...