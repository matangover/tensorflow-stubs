# Stubs for tensorflow.python.util.deprecation (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util import decorator_utils as decorator_utils, is_in_graph_mode as is_in_graph_mode, tf_contextlib as tf_contextlib, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from typing import Any as Any

class DeprecatedNamesAlreadySet(Exception): ...

def deprecated_alias(deprecated_name: Any, name: Any, func_or_class: Any, warn_once: bool = ...): ...
def deprecated_endpoints(*args: Any): ...
def deprecated(date: Any, instructions: Any, warn_once: bool = ...): ...

DeprecatedArgSpec = namedtuple('DeprecatedArgSpec', ['position', 'has_ok_value', 'ok_value'])

def deprecated_args(date: Any, instructions: Any, *deprecated_arg_names_or_tuples: Any, **kwargs: Any): ...
def deprecated_arg_values(date: Any, instructions: Any, warn_once: bool = ..., **deprecated_kwargs: Any): ...
def deprecated_argument_lookup(new_name: Any, new_value: Any, old_name: Any, old_value: Any): ...
def rewrite_argument_docstring(old_doc: Any, old_argument: Any, new_argument: Any): ...
def silence() -> None: ...
