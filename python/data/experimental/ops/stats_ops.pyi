# Stubs for tensorflow.python.data.experimental.ops.stats_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any

class StatsAggregator:
    def __init__(self) -> None: ...
    def get_summary(self): ...

class _SetStatsAggregatorDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, stats_aggregator: Any) -> None: ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def output_classes(self): ...

def set_stats_aggregator(stats_aggregator: Any): ...
def bytes_produced_stats(tag: Any): ...
def latency_stats(tag: Any): ...

class _StatsDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, op_function: Any, tag: Any) -> None: ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def output_classes(self): ...
