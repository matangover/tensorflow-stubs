# Stubs for tensorflow.python.estimator.training (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.framework import ops as ops
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, server_lib as server_lib, session_run_hook as session_run_hook
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import estimator_export as estimator_export
from typing import Any as Any, Optional as Optional

class TrainSpec:
    def __new__(cls, input_fn: Any, max_steps: Optional[Any] = ..., hooks: Optional[Any] = ...): ...

class EvalSpec:
    def __new__(cls, input_fn: Any, steps: int = ..., name: Optional[Any] = ..., hooks: Optional[Any] = ..., exporters: Optional[Any] = ..., start_delay_secs: int = ..., throttle_secs: int = ...): ...

def train_and_evaluate(estimator: Any, train_spec: Any, eval_spec: Any): ...

class _StopAtSecsHook(session_run_hook.SessionRunHook):
    def __init__(self, stop_after_secs: Any) -> None: ...
    def begin(self) -> None: ...
    def after_run(self, run_context: Any, run_values: Any) -> None: ...

class _NewCheckpointListenerForEvaluate(basic_session_run_hooks.CheckpointSaverListener):
    def __init__(self, evaluator: Any, eval_throttle_secs: Any, continuous_eval_listener: Any) -> None: ...
    def begin(self) -> None: ...
    def after_save(self, session: Any, global_step_value: Any): ...
    def end(self, session: Any, global_step_value: Any) -> None: ...

class _TrainingExecutor:
    def __init__(self, estimator: Any, train_spec: Any, eval_spec: Any, train_hooks: Optional[Any] = ..., continuous_eval_listener: Optional[Any] = ...) -> None: ...
    @property
    def estimator(self): ...
    def run(self): ...
    def run_chief(self): ...
    def run_worker(self): ...
    def run_master(self) -> None: ...
    def run_evaluator(self): ...
    def run_ps(self) -> None: ...
    def run_local(self): ...
    class _Evaluator:
        def __init__(self, estimator: Any, eval_spec: Any, max_training_steps: Any) -> None: ...
        @property
        def is_final_export_triggered(self): ...
        def evaluate_and_export(self): ...

class _EvalStatus:
    EVALUATED: str = ...
    MISSING_CHECKPOINT: str = ...
    NO_NEW_CHECKPOINT: str = ...

class _EvalResult:
    def __new__(cls, status: Any, metrics: Optional[Any] = ..., checkpoint_path: Optional[Any] = ...): ...

class _ContinuousEvalListener:
    def before_eval(self): ...
    def after_eval(self, eval_result: Any): ...
