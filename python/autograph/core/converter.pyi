# Stubs for tensorflow.python.autograph.core.converter (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from enum import Enum as Enum
from tensorflow.python.autograph.core import config as config, naming as naming
from tensorflow.python.autograph.pyct import anno as anno, ast_util as ast_util, cfg as cfg, compiler as compiler, qual_names as qual_names, transformer as transformer
from tensorflow.python.autograph.pyct.static_analysis import activity as activity, live_values as live_values, liveness as liveness, reaching_definitions as reaching_definitions, type_info as type_info
from typing import Any as Any

class ProgramContext:
    recursive: Any = ...
    autograph_decorators: Any = ...
    partial_types: Any = ...
    autograph_module: Any = ...
    uncompiled_modules: Any = ...
    conversion_order: Any = ...
    dependency_cache: Any = ...
    additional_imports: Any = ...
    name_map: Any = ...
    def __init__(self, recursive: Any, autograph_decorators: Any, partial_types: Any, autograph_module: Any, uncompiled_modules: Any) -> None: ...
    @property
    def required_imports(self): ...
    def new_namer(self, namespace: Any): ...
    def update_name_map(self, namer: Any) -> None: ...
    def add_to_cache(self, original_entity: Any, converted_ast: Any) -> None: ...

class EntityContext:
    namer: Any = ...
    info: Any = ...
    program: Any = ...
    def __init__(self, namer: Any, entity_info: Any, program_ctx: Any) -> None: ...

class Base(transformer.Base):
    ctx: Any = ...
    def __init__(self, ctx: Any) -> None: ...
    def get_definition_directive(self, node: Any, directive: Any, arg: Any, default: Any): ...
    def visit(self, node: Any): ...

class AnnotatedDef(reaching_definitions.Definition):
    directives: Any = ...
    def __init__(self) -> None: ...

class AgAnno(Enum):
    DIRECTIVES: str = ...

def standard_analysis(node: Any, context: Any, is_initial: bool = ...): ...
def apply_(node: Any, context: Any, converter_module: Any): ...