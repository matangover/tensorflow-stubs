# Stubs for tensorflow.contrib.linear_optimizer.python.sdca_optimizer (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib import layers as layers
from tensorflow.contrib.linear_optimizer.python.ops import sdca_ops as sdca_ops
from tensorflow.contrib.linear_optimizer.python.ops.sparse_feature_column import SparseFeatureColumn as SparseFeatureColumn
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

class SDCAOptimizer:
    def __init__(self, example_id_column: Any, num_loss_partitions: int = ..., num_table_shards: Optional[Any] = ..., symmetric_l1_regularization: float = ..., symmetric_l2_regularization: float = ..., adaptive: bool = ..., partitioner: Optional[Any] = ...) -> None: ...
    def get_name(self): ...
    @property
    def example_id_column(self): ...
    @property
    def num_loss_partitions(self): ...
    @property
    def num_table_shards(self): ...
    @property
    def symmetric_l1_regularization(self): ...
    @property
    def symmetric_l2_regularization(self): ...
    @property
    def adaptive(self): ...
    @property
    def partitioner(self): ...
    def get_train_step(self, columns_to_variables: Any, weight_column_name: Any, loss_type: Any, features: Any, targets: Any, global_step: Any): ...
