# Stubs for tensorflow.contrib.model_pruning.python.learning (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib import slim as _slim
from typing import Any as Any, Optional as Optional

train_step = _slim.learning.train_step

def train(train_op: Any, logdir: Any, mask_update_op: Any, train_step_fn: Any = ..., train_step_kwargs: Any = ..., log_every_n_steps: int = ..., graph: Optional[Any] = ..., master: str = ..., is_chief: bool = ..., global_step: Optional[Any] = ..., number_of_steps: Optional[Any] = ..., init_op: Any = ..., init_feed_dict: Optional[Any] = ..., local_init_op: Any = ..., init_fn: Optional[Any] = ..., ready_op: Any = ..., summary_op: Any = ..., save_summaries_secs: int = ..., summary_writer: Any = ..., startup_delay_steps: int = ..., saver: Optional[Any] = ..., save_interval_secs: int = ..., sync_optimizer: Optional[Any] = ..., session_config: Optional[Any] = ..., trace_every_n_steps: Optional[Any] = ...): ...