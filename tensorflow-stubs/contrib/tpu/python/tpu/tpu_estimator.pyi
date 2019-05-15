# Stubs for tensorflow.contrib.tpu.python.tpu.tpu_estimator (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.contrib.tpu.python.ops import tpu_ops as tpu_ops
from tensorflow.contrib.tpu.python.tpu import error_handling as error_handling, session_support as session_support, tpu as tpu, tpu_config as tpu_config, tpu_context as tpu_context, tpu_feed as tpu_feed, training_loop as training_loop
from tensorflow.contrib.training.python.training import hparam as hparam
from tensorflow.core.framework import variable_pb2 as variable_pb2
from tensorflow.core.framework.summary_pb2 import Summary as Summary
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.estimator import estimator as estimator_lib, model_fn as model_fn_lib
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.saved_model import tag_constants as tag_constants
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, evaluation as evaluation, session_run_hook as session_run_hook, training as training, training_util as training_util
from tensorflow.python.util import function_utils as function_utils, nest as nest, tf_inspect as tf_inspect
from typing import Any as Any, Optional as Optional

class _SIGNAL:
    NEXT_BATCH: int = ...
    STOP: int = ...

class TPUEstimatorSpec(model_fn_lib._TPUEstimatorSpec):
    def __new__(cls, mode: Any, predictions: Optional[Any] = ..., loss: Optional[Any] = ..., train_op: Optional[Any] = ..., eval_metrics: Optional[Any] = ..., export_outputs: Optional[Any] = ..., scaffold_fn: Optional[Any] = ..., host_call: Optional[Any] = ..., training_hooks: Optional[Any] = ..., evaluation_hooks: Optional[Any] = ..., prediction_hooks: Optional[Any] = ...): ...
    def as_estimator_spec(self): ...

class _OpQueueContext:
    def __init__(self, name: Any, target: Any, args: Any) -> None: ...
    def stop(self) -> None: ...
    def send_next_batch_signal(self, iterations: Any) -> None: ...
    def read_iteration_counts(self) -> None: ...
    def join(self) -> None: ...

class _OpSignalOnceQueueContext(_OpQueueContext):
    def __init__(self, name: Any, target: Any, args: Any) -> None: ...
    def send_next_batch_signal(self, iterations: Any) -> None: ...

class TPUInfeedOutfeedSessionHook(session_run_hook.SessionRunHook):
    def __init__(self, ctx: Any, enqueue_ops: Any, dequeue_ops: Any, run_infeed_loop_on_coordinator: bool = ..., rendezvous: Optional[Any] = ...) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def before_run(self, run_context: Any) -> None: ...
    def end(self, session: Any) -> None: ...

class TPUInfeedOutfeedSessionHookForPrediction(TPUInfeedOutfeedSessionHook):
    def __init__(self, ctx: Any, enqueue_ops: Any, dequeue_ops: Any, rendezvous: Optional[Any] = ...) -> None: ...

class _TPUStopAtStepHook(session_run_hook.SessionRunHook):
    def __init__(self, iterations: Any, num_steps: Optional[Any] = ..., last_step: Optional[Any] = ...) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def after_run(self, run_context: Any, run_values: Any) -> None: ...

class _SetEvalIterationsHook(session_run_hook.SessionRunHook):
    def __init__(self, num_steps: Any) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...

class _StoppingPredictHook(session_run_hook.SessionRunHook):
    def __init__(self, scalar_stopping_signal: Any) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def before_run(self, run_context: Any): ...
    def after_run(self, run_context: Any, run_values: Any) -> None: ...

def generate_per_core_enqueue_ops_fn_for_host(ctx: Any, input_fn: Any, inputs_structure_recorder: Any, host_device: Any, host_id: Any): ...
def generate_per_host_enqueue_ops_fn_for_host(ctx: Any, input_fn: Any, inputs_structure_recorder: Any, batch_axis: Any, device: Any, host_id: Any): ...
def generate_per_host_v2_enqueue_ops_fn_for_host(ctx: Any, input_fn: Any, inputs_structure_recorder: Any, device: Any, host_id: Any): ...
def generate_broadcast_enqueue_ops_fn(ctx: Any, input_fn: Any, inputs_structure_recorder: Any, num_hosts: Any): ...

class _InputPipeline:
    class InputsStructureRecorder:
        def __init__(self, input_partition_dims: Optional[Any] = ...) -> None: ...
        @property
        def flattened_input_dims(self): ...
        def has_labels(self): ...
        def validate_and_record_structure(self, features: Any, labels: Any) -> None: ...
        def flatten_features_and_labels(self, features: Any, labels: Any, signals: Optional[Any] = ...): ...
        def unflatten_features_and_labels(self, flattened_inputs: Any): ...
    def __init__(self, input_fn: Any, batch_axis: Any, ctx: Any) -> None: ...
    def generate_infeed_enqueue_ops_and_dequeue_fn(self): ...

class _ModelFnWrapper:
    def __init__(self, model_fn: Any, config: Any, params: Any, ctx: Any) -> None: ...
    def call_without_tpu(self, features: Any, labels: Any, is_export_mode: Any): ...
    def convert_to_single_tpu_train_step(self, dequeue_fn: Any): ...
    def convert_to_single_tpu_eval_step(self, dequeue_fn: Any): ...
    def convert_to_single_tpu_predict_step(self, dequeue_fn: Any): ...

class _OutfeedHostCall:
    def __init__(self, ctx: Any) -> None: ...
    @staticmethod
    def validate(host_calls: Any) -> None: ...
    @staticmethod
    def create_cpu_hostcall(host_calls: Any): ...
    def record(self, host_calls: Any) -> None: ...
    def create_enqueue_op(self): ...
    def create_tpu_hostcall(self): ...

class _OutfeedHostCallHook(session_run_hook.SessionRunHook):
    def __init__(self, tensors: Any) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def before_run(self, run_context: Any): ...
    def end(self, session: Any) -> None: ...

class ExamplesPerSecondHook(basic_session_run_hooks.StepCounterHook):
    def __init__(self, batch_size: Any, every_n_steps: int = ..., every_n_secs: Optional[Any] = ..., output_dir: Optional[Any] = ..., summary_writer: Optional[Any] = ...) -> None: ...

class InstallSignalHandlerHook(session_run_hook.SessionRunHook):
    def __init__(self) -> None: ...
    def before_run(self, run_context: Any) -> None: ...
    def end(self, session: Any) -> None: ...

class TPUEstimator(estimator_lib.Estimator):
    def __init__(self, model_fn: Optional[Any] = ..., model_dir: Optional[Any] = ..., config: Optional[Any] = ..., params: Optional[Any] = ..., use_tpu: bool = ..., train_batch_size: Optional[Any] = ..., eval_batch_size: Optional[Any] = ..., predict_batch_size: Optional[Any] = ..., batch_axis: Optional[Any] = ..., eval_on_tpu: bool = ..., export_to_tpu: bool = ..., warm_start_from: Optional[Any] = ...) -> None: ...
    def train(self, input_fn: Any, hooks: Optional[Any] = ..., steps: Optional[Any] = ..., max_steps: Optional[Any] = ..., saving_listeners: Optional[Any] = ...): ...
    def evaluate(self, input_fn: Any, steps: Optional[Any] = ..., hooks: Optional[Any] = ..., checkpoint_path: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def predict(self, input_fn: Any, predict_keys: Optional[Any] = ..., hooks: Optional[Any] = ..., checkpoint_path: Optional[Any] = ..., yield_single_examples: bool = ...) -> None: ...

class _CapturedObject:
    def __init__(self) -> None: ...
    def capture(self, o: Any) -> None: ...
    def get(self): ...

class _CapturingContext(control_flow_ops.ControlFlowContext, metaclass=abc.ABCMeta):
    def __init__(self, message: Any) -> None: ...
    def AddOp(self, op: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, _: Any, __: Any, ___: Any) -> None: ...

class _Inputs:
    def __init__(self, features: Optional[Any] = ..., labels: Optional[Any] = ..., dataset: Optional[Any] = ..., signals: Optional[Any] = ...) -> None: ...
    @staticmethod
    def from_input_fn(return_values: Any): ...
    @property
    def is_dataset(self): ...
    def dataset_initializer(self): ...
    def features_and_labels(self): ...
    def signals(self): ...
    @property
    def dataset(self): ...

class _InputsWithStoppingSignals(_Inputs):
    def __init__(self, dataset: Any, batch_size: Any, add_padding: bool = ..., num_invocations_per_step: int = ...) -> None: ...
    def features_and_labels(self): ...
    def signals(self): ...
    @staticmethod
    def insert_stopping_signal(stop: Any, batch_size: Any, add_padding: bool = ...): ...

class _StopSignals:
    NON_STOPPING_SIGNAL: bool = ...
    STOPPING_SIGNAL: bool = ...
    def __init__(self, stop: Any, batch_size: Any, padding_mask: Optional[Any] = ...) -> None: ...
    def as_dict(self): ...
    @staticmethod
    def as_scalar_stopping_signal(signals: Any): ...
    @staticmethod
    def should_stop(scalar_stopping_signal: Any): ...

class _PaddingSignals:
    @staticmethod
    def pad_features_and_labels(features: Any, labels: Any, batch_size: Any): ...
    @staticmethod
    def slice_tensor_or_dict(tensor_or_dict: Any, signals: Any): ...

def export_estimator_savedmodel(estimator: Any, export_dir_base: Any, serving_input_receiver_fn: Any, assets_extra: Optional[Any] = ..., as_text: bool = ..., checkpoint_path: Optional[Any] = ..., strip_default_attrs: bool = ...): ...