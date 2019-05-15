# Stubs for tensorflow.contrib.slim.python.slim.learning (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.training.python.training import training as training
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.client import timeline as timeline
from tensorflow.python.framework import constant_op as constant_op, errors as errors, ops as ops
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import clip_ops as clip_ops, control_flow_ops as control_flow_ops, lookup_ops as lookup_ops, math_ops as math_ops, variables as variables
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import supervisor as supervisor, sync_replicas_optimizer as sync_replicas_optimizer, training_util as training_util
from typing import Any as Any, Optional as Optional

def clip_gradient_norms(gradients_to_variables: Any, max_norm: Any): ...
def multiply_gradients(grads_and_vars: Any, gradient_multipliers: Any): ...
def add_gradients_summaries(grads_and_vars: Any): ...
def create_train_op(total_loss: Any, optimizer: Any, global_step: Any = ..., update_ops: Optional[Any] = ..., variables_to_train: Optional[Any] = ..., clip_gradient_norm: int = ..., summarize_gradients: bool = ..., gate_gradients: Any = ..., aggregation_method: Optional[Any] = ..., colocate_gradients_with_ops: bool = ..., gradient_multipliers: Optional[Any] = ..., check_numerics: bool = ...): ...
def train_step(sess: Any, train_op: Any, global_step: Any, train_step_kwargs: Any): ...
def train(train_op: Any, logdir: Any, train_step_fn: Any = ..., train_step_kwargs: Any = ..., log_every_n_steps: int = ..., graph: Optional[Any] = ..., master: str = ..., is_chief: bool = ..., global_step: Optional[Any] = ..., number_of_steps: Optional[Any] = ..., init_op: Any = ..., init_feed_dict: Optional[Any] = ..., local_init_op: Any = ..., init_fn: Optional[Any] = ..., ready_op: Any = ..., summary_op: Any = ..., save_summaries_secs: int = ..., summary_writer: Any = ..., startup_delay_steps: int = ..., saver: Optional[Any] = ..., save_interval_secs: int = ..., sync_optimizer: Optional[Any] = ..., session_config: Optional[Any] = ..., session_wrapper: Optional[Any] = ..., trace_every_n_steps: Optional[Any] = ..., ignore_live_threads: bool = ...): ...