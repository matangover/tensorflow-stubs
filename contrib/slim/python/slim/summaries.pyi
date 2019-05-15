# Stubs for tensorflow.contrib.slim.python.slim.summaries (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import logging_ops as logging_ops
from tensorflow.python.summary import summary as summary
from typing import Any as Any, Optional as Optional

def add_histogram_summary(tensor: Any, name: Optional[Any] = ..., prefix: Optional[Any] = ...): ...
def add_image_summary(tensor: Any, name: Optional[Any] = ..., prefix: Optional[Any] = ..., print_summary: bool = ...): ...
def add_scalar_summary(tensor: Any, name: Optional[Any] = ..., prefix: Optional[Any] = ..., print_summary: bool = ...): ...
def add_zero_fraction_summary(tensor: Any, name: Optional[Any] = ..., prefix: Optional[Any] = ..., print_summary: bool = ...): ...
def add_histogram_summaries(tensors: Any, prefix: Optional[Any] = ...): ...
def add_image_summaries(tensors: Any, prefix: Optional[Any] = ...): ...
def add_scalar_summaries(tensors: Any, prefix: Optional[Any] = ..., print_summary: bool = ...): ...
def add_zero_fraction_summaries(tensors: Any, prefix: Optional[Any] = ...): ...
