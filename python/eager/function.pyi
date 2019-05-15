# Stubs for tensorflow.python.eager.function (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, function_pb2 as function_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.eager import context as context, execute as execute, tape as tape
from tensorflow.python.eager.graph_only_ops import graph_placeholder as graph_placeholder
from tensorflow.python.framework import c_api_util as c_api_util, constant_op as constant_op, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, cond_v2_impl as cond_v2_impl, control_flow_ops as control_flow_ops, functional_ops as functional_ops, gradients_impl as gradients_impl, resource_variable_ops as resource_variable_ops, variable_scope as variable_scope
from tensorflow.python.training import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.util import compat as compat, nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from typing import Any as Any, Optional as Optional

FORWARD_FUNCTION_ATTRIBUTE_NAME: str
BACKWARD_FUNCTION_ATTRIBUTE_NAME: str
WHITELIST_FUNCTION_ATTRIBUTE_REGEX: Any

class FuncGraph(ops.Graph):
    name: Any = ...
    inputs: Any = ...
    outputs: Any = ...
    structured_outputs: Any = ...
    outer_graph: Any = ...
    captures: Any = ...
    seed: Any = ...
    def __init__(self, name: Any) -> None: ...
    @property
    def variables(self) -> None: ...
    @variables.setter
    def variables(self, var_list: Any) -> None: ...
    def control_dependencies(self, control_inputs: Any): ...
    def create_op(self, op_type: Any, inputs: Any, dtypes: Any, input_types: Optional[Any] = ..., name: Optional[Any] = ..., attrs: Optional[Any] = ..., op_def: Optional[Any] = ..., compute_shapes: bool = ..., compute_device: bool = ...): ...
    def capture(self, tensor: Any, name: Optional[Any] = ...): ...
    @property
    def external_captures(self): ...
    @property
    def internal_captures(self): ...

class _EagerDefinedFunction:
    definition: Any = ...
    name: Any = ...
    signature: Any = ...
    grad_func_name: Any = ...
    python_grad_func: Any = ...
    def __init__(self, name: Any, graph: Any, inputs: Any, outputs: Any, attrs: Any) -> None: ...
    def add_to_graph(self, g: Any) -> None: ...
    @property
    def stateful_ops(self): ...
    def call(self, ctx: Any, args: Any): ...

class Function:
    def __init__(self, func_graph: Any, attrs: Optional[Any] = ...) -> None: ...
    def __call__(self, *args: Any): ...
    @property
    def graph(self): ...
    @property
    def inputs(self): ...
    @property
    def outputs(self): ...
    @property
    def captured_inputs(self): ...
    @property
    def function_def(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_dtypes(self): ...

def func_graph_from_py_func(name: Any, python_func: Any, args: Any, kwargs: Any, signature: Optional[Any] = ..., func_graph: Optional[Any] = ...): ...

class PolymorphicFunction:
    def __init__(self, python_function: Any, name: Any, input_signature: Optional[Any] = ..., attributes: Optional[Any] = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    @property
    def python_function(self): ...
    def get_concrete_function(self, *args: Any, **kwargs: Any): ...
    def __get__(self, instance: Any, owner: Any): ...

def register(func: Any, *args: Any, **kwargs: Any): ...
def defun(func: Optional[Any] = ..., input_signature: Optional[Any] = ...): ...
def defun_with_attributes(func: Optional[Any] = ..., input_signature: Optional[Any] = ..., attributes: Optional[Any] = ...): ...

class AutomaticControlDependencies:
    def __init__(self) -> None: ...
    def mark_as_return(self, tensor: Any): ...
    def __enter__(self): ...
    def __exit__(self, unused_type: Any, unused_value: Any, unused_traceback: Any) -> None: ...

def automatic_control_dependencies(f: Any): ...
