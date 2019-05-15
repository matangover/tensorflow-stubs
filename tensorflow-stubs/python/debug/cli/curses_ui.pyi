# Stubs for tensorflow.python.debug.cli.curses_ui (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.debug.cli import base_ui as base_ui, cli_shared as cli_shared, command_parser as command_parser, curses_widgets as curses_widgets, debugger_cli_common as debugger_cli_common, tensor_format as tensor_format
from typing import Any as Any, Optional as Optional

class ScrollBar:
    BASE_ATTR: Any = ...
    def __init__(self, min_x: Any, min_y: Any, max_x: Any, max_y: Any, scroll_position: Any, output_num_rows: Any) -> None: ...
    def layout(self): ...
    def get_click_command(self, mouse_y: Any): ...

class CursesUI(base_ui.BaseUI):
    CLI_TERMINATOR_KEY: int = ...
    CLI_TAB_KEY: Any = ...
    BACKSPACE_KEY: Any = ...
    REGEX_SEARCH_PREFIX: str = ...
    TENSOR_INDICES_NAVIGATION_PREFIX: str = ...
    CLI_CR_KEYS: Any = ...
    def __init__(self, on_ui_exit: Optional[Any] = ..., config: Optional[Any] = ...) -> None: ...
    def run_ui(self, init_command: Optional[Any] = ..., title: Optional[Any] = ..., title_color: Optional[Any] = ..., enable_mouse_on_start: bool = ...): ...
    def get_help(self): ...