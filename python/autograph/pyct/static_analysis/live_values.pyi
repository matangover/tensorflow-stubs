# Stubs for tensorflow.python.autograph.pyct.static_analysis.live_values (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.autograph.pyct import anno as anno, transformer as transformer
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno
from typing import Any as Any

class LiveValueResolver(transformer.Base):
    literals: Any = ...
    def __init__(self, context: Any, literals: Any) -> None: ...
    def visit_ClassDef(self, node: Any): ...
    def visit_Name(self, node: Any): ...
    def visit_Attribute(self, node: Any): ...

def resolve(node: Any, context: Any, literals: Any): ...
