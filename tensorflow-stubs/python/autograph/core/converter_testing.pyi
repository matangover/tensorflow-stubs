# Stubs for tensorflow.python.autograph.core.converter_testing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.autograph import operators as operators, utils as utils
from tensorflow.python.autograph.core import config as config, converter as converter, errors as errors, function_wrapping as function_wrapping
from tensorflow.python.autograph.pyct import compiler as compiler, parser as parser, pretty_printer as pretty_printer, transformer as transformer
from tensorflow.python.platform import test as test
from typing import Any as Any, Optional as Optional

def imported_decorator(f: Any): ...

class FakeNamer:
    i: int = ...
    def __init__(self) -> None: ...
    def new_symbol(self, name_root: Any, used: Any): ...
    def compiled_function_name(self, original_fqn: Any, live_entity: Optional[Any] = ..., owner_type: Optional[Any] = ...): ...

class FakeNoRenameNamer(FakeNamer):
    def compiled_function_name(self, original_fqn: Any, **_: Any): ...

class TestCase(test.TestCase):
    def assertPrints(self, expected_result: Any) -> None: ...
    dynamic_calls: Any = ...
    recursive: Any = ...
    def compiled(self, node: Any, namespace: Any, *symbols: Any): ...
    def converted(self, entity: Any, converter_module: Any, namespace: Any, *tf_symbols: Any) -> None: ...
    def make_fake_mod(self, name: Any, *symbols: Any): ...
    def attach_namespace(self, module: Any, **ns: Any) -> None: ...
    def prepare(self, test_fn: Any, namespace: Any, namer: Optional[Any] = ..., arg_types: Optional[Any] = ..., owner_type: Optional[Any] = ..., recursive: bool = ..., autograph_decorators: Any = ...): ...
