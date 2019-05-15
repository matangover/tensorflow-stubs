# Stubs for tensorflow.python.debug.cli.debugger_cli_common (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python import pywrap_tensorflow_internal as pywrap_tensorflow_internal
from tensorflow.python.platform import gfile as gfile
from typing import Any as Any, Optional as Optional

HELP_INDENT: str
EXPLICIT_USER_EXIT: str
REGEX_MATCH_LINES_KEY: str
INIT_SCROLL_POS_KEY: str
MAIN_MENU_KEY: str

class CommandLineExit(Exception):
    def __init__(self, exit_token: Optional[Any] = ...) -> None: ...
    @property
    def exit_token(self): ...

class RichLine:
    text: Any = ...
    font_attr_segs: Any = ...
    def __init__(self, text: str = ..., font_attr: Optional[Any] = ...) -> None: ...
    def __add__(self, other: Any): ...
    def __len__(self): ...

def rich_text_lines_from_rich_line_list(rich_text_list: Any, annotations: Optional[Any] = ...): ...
def get_tensorflow_version_lines(include_dependency_versions: bool = ...): ...

class RichTextLines:
    def __init__(self, lines: Any, font_attr_segs: Optional[Any] = ..., annotations: Optional[Any] = ...) -> None: ...
    @property
    def lines(self): ...
    @property
    def font_attr_segs(self): ...
    @property
    def annotations(self): ...
    def num_lines(self): ...
    def slice(self, begin: Any, end: Any): ...
    def extend(self, other: Any) -> None: ...
    def append(self, line: Any, font_attr_segs: Optional[Any] = ...) -> None: ...
    def append_rich_line(self, rich_line: Any) -> None: ...
    def prepend(self, line: Any, font_attr_segs: Optional[Any] = ...) -> None: ...
    def write_to_file(self, file_path: Any) -> None: ...

def regex_find(orig_screen_output: Any, regex: Any, font_attr: Any): ...
def wrap_rich_text_lines(inp: Any, cols: Any): ...

class CommandHandlerRegistry:
    HELP_COMMAND: str = ...
    HELP_COMMAND_ALIASES: Any = ...
    VERSION_COMMAND: str = ...
    VERSION_COMMAND_ALIASES: Any = ...
    def __init__(self) -> None: ...
    def register_command_handler(self, prefix: Any, handler: Any, help_info: Any, prefix_aliases: Optional[Any] = ...) -> None: ...
    def dispatch_command(self, prefix: Any, argv: Any, screen_info: Optional[Any] = ...): ...
    def is_registered(self, prefix: Any): ...
    def get_help(self, cmd_prefix: Optional[Any] = ...): ...
    def set_help_intro(self, help_intro: Any) -> None: ...

class TabCompletionRegistry:
    def __init__(self) -> None: ...
    def register_tab_comp_context(self, context_words: Any, comp_items: Any) -> None: ...
    def deregister_context(self, context_words: Any) -> None: ...
    def extend_comp_items(self, context_word: Any, new_comp_items: Any) -> None: ...
    def remove_comp_items(self, context_word: Any, comp_items: Any) -> None: ...
    def get_completions(self, context_word: Any, prefix: Any): ...

class CommandHistory:
    def __init__(self, limit: int = ..., history_file_path: Optional[Any] = ...) -> None: ...
    def add_command(self, command: Any) -> None: ...
    def most_recent_n(self, n: Any): ...
    def lookup_prefix(self, prefix: Any, n: Any): ...

class MenuItem:
    def __init__(self, caption: Any, content: Any, enabled: bool = ...) -> None: ...
    @property
    def caption(self): ...
    @property
    def type(self): ...
    @property
    def content(self): ...
    def is_enabled(self): ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...

class Menu:
    def __init__(self, name: Optional[Any] = ...) -> None: ...
    def append(self, item: Any) -> None: ...
    def insert(self, index: Any, item: Any) -> None: ...
    def num_items(self): ...
    def captions(self): ...
    def caption_to_item(self, caption: Any): ...
    def format_as_single_line(self, prefix: Optional[Any] = ..., divider: str = ..., enabled_item_attrs: Optional[Any] = ..., disabled_item_attrs: Optional[Any] = ...): ...