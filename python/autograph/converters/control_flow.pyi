# Stubs for tensorflow.python.autograph.converters.control_flow (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, ast_util as ast_util, parser as parser, templates as templates
from tensorflow.python.autograph.pyct.static_analysis import annos as annos
from typing import Any as Any

class SymbolNamer:
    def new_symbol(self, name_root: Any, reserved_locals: Any) -> None: ...

class ControlFlowTransformer(converter.Base):
    def visit_If(self, node: Any): ...
    def visit_While(self, node: Any): ...
    def visit_For(self, node: Any): ...

def transform(node: Any, ctx: Any): ...
