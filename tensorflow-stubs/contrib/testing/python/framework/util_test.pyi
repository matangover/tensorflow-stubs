# Stubs for tensorflow.contrib.testing.python.framework.util_test (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import summary_pb2 as summary_pb2
from tensorflow.python.training import summary_io as summary_io
from typing import Any as Any

def assert_summary(expected_tags: Any, expected_simple_values: Any, summary_proto: Any) -> None: ...
def to_summary_proto(summary_str: Any): ...
def latest_event_file(base_dir: Any): ...
def latest_events(base_dir: Any): ...
def latest_summaries(base_dir: Any): ...
def simple_values_from_events(events: Any, tags: Any): ...
