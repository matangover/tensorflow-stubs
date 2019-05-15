# Stubs for tensorflow.contrib.learn.python.learn.graph_actions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.framework import load_variable as load_variable
from tensorflow.core.framework import summary_pb2 as summary_pb2
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, logging_ops as logging_ops, lookup_ops as lookup_ops, resources as resources, variables as variables
from tensorflow.python.training import coordinator as coordinator, queue_runner as queue_runner, summary_io as summary_io
from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any as Any, Optional as Optional

def clear_summary_writers(): ...
def get_summary_writer(logdir: Any): ...
def train(graph: Any, output_dir: Any, train_op: Any, loss_op: Any, global_step_tensor: Optional[Any] = ..., init_op: Optional[Any] = ..., init_feed_dict: Optional[Any] = ..., init_fn: Optional[Any] = ..., log_every_steps: int = ..., supervisor_is_chief: bool = ..., supervisor_master: str = ..., supervisor_save_model_secs: int = ..., keep_checkpoint_max: int = ..., supervisor_save_summaries_steps: int = ..., feed_fn: Optional[Any] = ..., steps: Optional[Any] = ..., fail_on_nan_loss: bool = ..., monitors: Optional[Any] = ..., max_steps: Optional[Any] = ...): ...
def evaluate(graph: Any, output_dir: Any, checkpoint_path: Any, eval_dict: Any, update_op: Optional[Any] = ..., global_step_tensor: Optional[Any] = ..., supervisor_master: str = ..., log_every_steps: int = ..., feed_fn: Optional[Any] = ..., max_steps: Optional[Any] = ...): ...
def run_n(output_dict: Any, feed_dict: Optional[Any] = ..., restore_checkpoint_path: Optional[Any] = ..., n: int = ...): ...
def run_feeds_iter(output_dict: Any, feed_dicts: Any, restore_checkpoint_path: Optional[Any] = ...) -> None: ...
def run_feeds(*args: Any, **kwargs: Any): ...
def infer(restore_checkpoint_path: Any, output_dict: Any, feed_dict: Optional[Any] = ...): ...
