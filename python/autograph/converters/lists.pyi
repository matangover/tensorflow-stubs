# Stubs for tensorflow.python.autograph.converters.lists (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.lang import directives as directives
from tensorflow.python.autograph.pyct import anno as anno, parser as parser, templates as templates
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno
from typing import Any as Any

POP_USES: str

class ListTransformer(converter.Base):
    def visit_List(self, node: Any): ...
    def visit_Call(self, node: Any): ...
    def visit_FunctionDef(self, node: Any): ...
    def visit_For(self, node: Any): ...
    def visit_While(self, node: Any): ...
    def visit_If(self, node: Any): ...
    def visit_With(self, node: Any): ...

def transform(node: Any, ctx: Any): ...
