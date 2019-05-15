# Stubs for tensorflow.contrib.distribute.python.collective_all_reduce_strategy (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.distribute.python import cross_tower_utils as cross_tower_utils, mirrored_strategy as mirrored_strategy, values as values
from tensorflow.core.protobuf import rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python.distribute import multi_worker_util as multi_worker_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, collective_ops as collective_ops
from typing import Any as Any, Optional as Optional

class CollectiveAllReduceStrategy(mirrored_strategy.MirroredStrategy):
    def __init__(self, num_gpus_per_worker: int = ...) -> None: ...
    def distribute_dataset(self, dataset_fn: Any): ...
    def configure(self, session_config: Optional[Any] = ..., cluster_spec: Optional[Any] = ..., task_type: Optional[Any] = ..., task_id: Optional[Any] = ...) -> None: ...
    @property
    def between_graph(self): ...
    @property
    def should_init(self): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...
