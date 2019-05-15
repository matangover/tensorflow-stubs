# Stubs for tensorflow.python.autograph.pyct.anno (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import enum as enum
from typing import Any as Any

class NoValue(enum.Enum): ...

class Basic(NoValue):
    QN: str = ...
    SKIP_PROCESSING: str = ...
    INDENT_BLOCK_REMAINDER: str = ...
    ORIGIN: str = ...

class Static(NoValue):
    IS_LOCAL: str = ...
    IS_PARAM: str = ...
    SCOPE: str = ...
    ARGS_SCOPE: str = ...
    COND_SCOPE: str = ...
    BODY_SCOPE: str = ...
    ORELSE_SCOPE: str = ...
    DEFINITIONS: str = ...
    ORIG_DEFINITIONS: str = ...
    DEFINED_VARS_IN: str = ...
    LIVE_VARS_OUT: str = ...

FAIL: Any

def keys(node: Any, field_name: str = ...): ...
def getanno(node: Any, key: Any, default: Any = ..., field_name: str = ...): ...
def hasanno(node: Any, key: Any, field_name: str = ...): ...
def setanno(node: Any, key: Any, value: Any, field_name: str = ...) -> None: ...
def delanno(node: Any, key: Any, field_name: str = ...) -> None: ...
def copyanno(from_node: Any, to_node: Any, key: Any, field_name: str = ...) -> None: ...
def dup(node: Any, copy_map: Any, field_name: str = ...) -> None: ...
