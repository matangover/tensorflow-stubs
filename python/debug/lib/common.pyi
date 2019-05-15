# Stubs for tensorflow.python.debug.lib.common (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from typing import Any as Any

GRPC_URL_PREFIX: str

RunKey = namedtuple('RunKey', ['feed_names', 'fetch_names'])

def get_graph_element_name(elem: Any): ...
def get_flattened_names(feeds_or_fetches: Any): ...
def get_run_key(feed_dict: Any, fetches: Any): ...
