# Stubs for tensorflow.contrib.training.python.training.evaluation (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops import state_ops as state_ops
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, checkpoint_management as checkpoint_management, evaluation as evaluation, monitored_session as monitored_session, session_run_hook as session_run_hook, training_util as training_util
from typing import Any as Any, Optional as Optional

StopAfterNEvalsHook: Any
evaluate_once: Any
get_or_create_eval_step: Any

def wait_for_new_checkpoint(checkpoint_dir: Any, last_checkpoint: Optional[Any] = ..., seconds_to_sleep: int = ..., timeout: Optional[Any] = ...): ...
def checkpoints_iterator(checkpoint_dir: Any, min_interval_secs: int = ..., timeout: Optional[Any] = ..., timeout_fn: Optional[Any] = ...) -> None: ...

class SummaryAtEndHook(session_run_hook.SessionRunHook):
    def __init__(self, log_dir: Optional[Any] = ..., summary_writer: Optional[Any] = ..., summary_op: Optional[Any] = ..., feed_dict: Optional[Any] = ...) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def end(self, session: Any) -> None: ...

def evaluate_repeatedly(checkpoint_dir: Any, master: str = ..., scaffold: Optional[Any] = ..., eval_ops: Optional[Any] = ..., feed_dict: Optional[Any] = ..., final_ops: Optional[Any] = ..., final_ops_feed_dict: Optional[Any] = ..., eval_interval_secs: int = ..., hooks: Optional[Any] = ..., config: Optional[Any] = ..., max_number_of_evaluations: Optional[Any] = ..., timeout: Optional[Any] = ..., timeout_fn: Optional[Any] = ...): ...