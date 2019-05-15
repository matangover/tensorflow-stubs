# Stubs for tensorflow.contrib.estimator.python.estimator.hooks (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, state_ops as state_ops
from tensorflow.python.training import training as training, training_util as training_util
from typing import Any as Any, Optional as Optional

class InMemoryEvaluatorHook(training.SessionRunHook):
    def __init__(self, estimator: Any, input_fn: Any, steps: Optional[Any] = ..., hooks: Optional[Any] = ..., name: Optional[Any] = ..., every_n_iter: int = ...) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def after_run(self, run_context: Any, run_values: Any) -> None: ...
    def end(self, session: Any) -> None: ...

class _StopAtCheckpointStepHook(training.SessionRunHook):
    def __init__(self, model_dir: Any, last_step: Any, wait_after_file_check_secs: int = ...) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context: Any): ...
    def after_run(self, run_context: Any, run_values: Any) -> None: ...

def make_stop_at_checkpoint_step_hook(estimator: Any, last_step: Any, wait_after_file_check_secs: int = ...): ...
