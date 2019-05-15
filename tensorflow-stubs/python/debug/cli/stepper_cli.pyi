# Stubs for tensorflow.python.debug.cli.stepper_cli (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.debug.cli import cli_shared as cli_shared, command_parser as command_parser, debugger_cli_common as debugger_cli_common, tensor_format as tensor_format
from tensorflow.python.debug.lib import stepper as stepper
from typing import Any as Any, Optional as Optional

RL = debugger_cli_common.RichLine

class NodeStepperCLI:
    STATE_CONT: str = ...
    STATE_DUMPED_INTERMEDIATE: str = ...
    STATE_OVERRIDDEN: str = ...
    STATE_IS_PLACEHOLDER: str = ...
    STATE_DIRTY_VARIABLE: str = ...
    STATE_UNFEEDABLE: str = ...
    NEXT_NODE_POINTER_STR: str = ...
    arg_parsers: Any = ...
    def __init__(self, node_stepper: Any) -> None: ...
    def list_sorted_nodes(self, args: Any, screen_info: Optional[Any] = ...): ...
    def cont(self, args: Any, screen_info: Optional[Any] = ...): ...
    def step(self, args: Any, screen_info: Optional[Any] = ...): ...
    def print_tensor(self, args: Any, screen_info: Optional[Any] = ...): ...
    def inject_value(self, args: Any, screen_info: Optional[Any] = ...): ...