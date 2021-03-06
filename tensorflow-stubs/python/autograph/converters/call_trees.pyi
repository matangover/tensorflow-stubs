# Stubs for tensorflow.python.autograph.converters.call_trees (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, ast_util as ast_util, inspect_utils as inspect_utils, parser as parser, templates as templates
from tensorflow.python.util import tf_inspect as tf_inspect
from typing import Any as Any, Optional as Optional

class FunctionInfo: ...

KNOWN_NUMPY_FUNCTIONS: Any

class FunctionNamer:
    def compiled_function_name(self, original_fqn: Any, live_entity: Optional[Any] = ..., owner_type: Optional[Any] = ...) -> None: ...
    def compiled_class_name(self, original_fqn: Any, live_entity: Optional[Any] = ...) -> None: ...

class CallTreeTransformer(converter.Base):
    def visit_Expr(self, node: Any): ...
    def visit_Call(self, node: Any): ...

def transform(node: Any, ctx: Any): ...
