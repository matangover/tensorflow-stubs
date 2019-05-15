# Stubs for tensorflow.python.ops.template (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import variable_scope as variable_scope
from tensorflow.python.training.checkpointable import base as checkpointable
from tensorflow.python.util import tf_contextlib as tf_contextlib, tf_decorator as tf_decorator
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def make_template(name_: Any, func_: Any, create_scope_now_: bool = ..., unique_name_: Optional[Any] = ..., custom_getter_: Optional[Any] = ..., **kwargs: Any): ...

class Template(checkpointable.CheckpointableBase):
    def __init__(self, name: Any, func: Any, create_scope_now: bool = ..., unique_name: Optional[Any] = ..., custom_getter: Optional[Any] = ..., create_graph_function: bool = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    @property
    def name(self): ...
    @property
    def func(self): ...
    @property
    def variable_scope(self): ...
    @property
    def variable_scope_name(self): ...
    @property
    def variables(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def global_variables(self): ...
    @property
    def local_variables(self): ...
    @property
    def weights(self): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def var_scope(self): ...

class _EagerTemplateVariableStore:
    def __init__(self, variable_scope_name: Any) -> None: ...
    def set_variable_scope_name(self, variable_scope_name: Any) -> None: ...
    def as_default(self) -> None: ...
    def variables(self): ...
    def trainable_variables(self): ...
    def non_trainable_variables(self): ...

class EagerTemplate(Template):
    def __init__(self, name: Any, func: Any, create_scope_now: bool = ..., custom_getter: Optional[Any] = ..., create_graph_function: bool = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    @property
    def name(self): ...
    @property
    def func(self): ...
    @property
    def variable_scope(self): ...
    @property
    def variable_scope_name(self): ...
    @property
    def variables(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def global_variables(self): ...
    @property
    def local_variables(self): ...