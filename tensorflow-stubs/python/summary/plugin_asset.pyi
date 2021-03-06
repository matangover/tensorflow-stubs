# Stubs for tensorflow.python.summary.plugin_asset (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.python.framework import ops as ops
from typing import Any as Any, Optional as Optional

def get_plugin_asset(plugin_asset_cls: Any, graph: Optional[Any] = ...): ...
def get_all_plugin_assets(graph: Optional[Any] = ...): ...

class PluginAsset(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    plugin_name: Any = ...
    @abc.abstractmethod
    def assets(self) -> Any: ...
