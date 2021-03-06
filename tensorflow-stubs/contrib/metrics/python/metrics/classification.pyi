# Stubs for tensorflow.contrib.metrics.python.metrics.classification (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, metrics_impl as metrics_impl, variable_scope as variable_scope
from tensorflow.python.training import distribution_strategy_context as distribution_strategy_context
from typing import Any as Any, Optional as Optional

def accuracy(predictions: Any, labels: Any, weights: Optional[Any] = ..., name: Optional[Any] = ...): ...
def f1_score(labels: Any, predictions: Any, weights: Optional[Any] = ..., num_thresholds: int = ..., metrics_collections: Optional[Any] = ..., updates_collections: Optional[Any] = ..., name: Optional[Any] = ...): ...
