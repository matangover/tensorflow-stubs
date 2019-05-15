# Stubs for tensorflow.python.autograph.converters.break_statements (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, templates as templates
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno
from typing import Any as Any

class _Break:
    used: bool = ...
    control_var_name: Any = ...
    def __init__(self) -> None: ...

class BreakTransformer(converter.Base):
    def visit_Break(self, node: Any): ...
    def visit_While(self, node: Any): ...
    def visit_For(self, node: Any): ...

def transform(node: Any, ctx: Any): ...
