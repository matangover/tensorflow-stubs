# Stubs for tensorflow.python.keras.callbacks (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.data.ops import iterator_ops as iterator_ops
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras.engine.training_utils import standardize_input_data as standardize_input_data
from tensorflow.python.keras.utils.data_utils import Sequence as Sequence
from tensorflow.python.keras.utils.generic_utils import Progbar as Progbar
from tensorflow.python.ops import array_ops as array_ops, state_ops as state_ops, summary_ops_v2 as summary_ops_v2, variables as variables
from tensorflow.python.training import saver as saver
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def configure_callbacks(callbacks: Any, model: Any, do_validation: bool = ..., val_inputs: Optional[Any] = ..., val_targets: Optional[Any] = ..., val_sample_weights: Optional[Any] = ..., batch_size: Optional[Any] = ..., epochs: Optional[Any] = ..., steps_per_epoch: Optional[Any] = ..., samples: Optional[Any] = ..., validation_steps: Optional[Any] = ..., verbose: int = ..., count_mode: str = ...): ...

class CallbackList:
    callbacks: Any = ...
    queue_length: Any = ...
    params: Any = ...
    model: Any = ...
    def __init__(self, callbacks: Optional[Any] = ..., queue_length: int = ...) -> None: ...
    def append(self, callback: Any) -> None: ...
    def set_params(self, params: Any) -> None: ...
    def set_model(self, model: Any) -> None: ...
    def on_epoch_begin(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_batch_begin(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_batch_end(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    def on_train_end(self, logs: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...

class Callback:
    validation_data: Any = ...
    model: Any = ...
    def __init__(self) -> None: ...
    params: Any = ...
    def set_params(self, params: Any) -> None: ...
    def set_model(self, model: Any) -> None: ...
    def on_epoch_begin(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_batch_begin(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_batch_end(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    def on_train_end(self, logs: Optional[Any] = ...) -> None: ...

class BaseLogger(Callback):
    stateful_metrics: Any = ...
    def __init__(self, stateful_metrics: Optional[Any] = ...) -> None: ...
    seen: int = ...
    totals: Any = ...
    def on_epoch_begin(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_batch_end(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...

class TerminateOnNaN(Callback):
    def on_batch_end(self, batch: Any, logs: Optional[Any] = ...) -> None: ...

class ProgbarLogger(Callback):
    use_steps: bool = ...
    stateful_metrics: Any = ...
    def __init__(self, count_mode: str = ..., stateful_metrics: Optional[Any] = ...) -> None: ...
    verbose: Any = ...
    epochs: Any = ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    target: Any = ...
    progbar: Any = ...
    seen: int = ...
    def on_epoch_begin(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    log_values: Any = ...
    def on_batch_begin(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_batch_end(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...

class History(Callback):
    epoch: Any = ...
    history: Any = ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...

class ModelCheckpoint(Callback):
    monitor: Any = ...
    verbose: Any = ...
    filepath: Any = ...
    save_best_only: Any = ...
    save_weights_only: Any = ...
    period: Any = ...
    epochs_since_last_save: int = ...
    monitor_op: Any = ...
    best: Any = ...
    def __init__(self, filepath: Any, monitor: str = ..., verbose: int = ..., save_best_only: bool = ..., save_weights_only: bool = ..., mode: str = ..., period: int = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...

class EarlyStopping(Callback):
    monitor: Any = ...
    patience: Any = ...
    verbose: Any = ...
    baseline: Any = ...
    min_delta: Any = ...
    wait: int = ...
    stopped_epoch: int = ...
    monitor_op: Any = ...
    def __init__(self, monitor: str = ..., min_delta: int = ..., patience: int = ..., verbose: int = ..., mode: str = ..., baseline: Optional[Any] = ...) -> None: ...
    best: Any = ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_train_end(self, logs: Optional[Any] = ...) -> None: ...

class RemoteMonitor(Callback):
    root: Any = ...
    path: Any = ...
    field: Any = ...
    headers: Any = ...
    send_as_json: Any = ...
    def __init__(self, root: str = ..., path: str = ..., field: str = ..., headers: Optional[Any] = ..., send_as_json: bool = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...

class LearningRateScheduler(Callback):
    schedule: Any = ...
    verbose: Any = ...
    def __init__(self, schedule: Any, verbose: int = ...) -> None: ...
    def on_epoch_begin(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...

class TensorBoard(Callback):
    log_dir: Any = ...
    histogram_freq: Any = ...
    merged: Any = ...
    write_graph: Any = ...
    write_grads: Any = ...
    write_images: Any = ...
    batch_size: Any = ...
    embeddings_freq: Any = ...
    embeddings_layer_names: Any = ...
    embeddings_metadata: Any = ...
    embeddings_data: Any = ...
    def __init__(self, log_dir: str = ..., histogram_freq: int = ..., batch_size: int = ..., write_graph: bool = ..., write_grads: bool = ..., write_images: bool = ..., embeddings_freq: int = ..., embeddings_layer_names: Optional[Any] = ..., embeddings_metadata: Optional[Any] = ..., embeddings_data: Optional[Any] = ...) -> None: ...
    model: Any = ...
    assign_embeddings: Any = ...
    batch_id: Any = ...
    step: Any = ...
    saver: Any = ...
    def set_model(self, model: Any) -> None: ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    def on_batch_end(self, batch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_begin(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def on_train_end(self, logs: Optional[Any] = ...) -> None: ...

class ReduceLROnPlateau(Callback):
    monitor: Any = ...
    factor: Any = ...
    min_lr: Any = ...
    min_delta: Any = ...
    patience: Any = ...
    verbose: Any = ...
    cooldown: Any = ...
    cooldown_counter: int = ...
    wait: int = ...
    best: int = ...
    mode: Any = ...
    monitor_op: Any = ...
    def __init__(self, monitor: str = ..., factor: float = ..., patience: int = ..., verbose: int = ..., mode: str = ..., min_delta: float = ..., cooldown: int = ..., min_lr: int = ..., **kwargs: Any) -> None: ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...) -> None: ...
    def in_cooldown(self): ...

class CSVLogger(Callback):
    sep: Any = ...
    filename: Any = ...
    append: Any = ...
    writer: Any = ...
    keys: Any = ...
    append_header: bool = ...
    file_flags: Any = ...
    def __init__(self, filename: Any, separator: str = ..., append: bool = ...) -> None: ...
    csv_file: Any = ...
    def on_train_begin(self, logs: Optional[Any] = ...) -> None: ...
    def on_epoch_end(self, epoch: Any, logs: Optional[Any] = ...): ...
    def on_train_end(self, logs: Optional[Any] = ...) -> None: ...

class LambdaCallback(Callback):
    on_epoch_begin: Any = ...
    on_epoch_end: Any = ...
    on_batch_begin: Any = ...
    on_batch_end: Any = ...
    on_train_begin: Any = ...
    on_train_end: Any = ...
    def __init__(self, on_epoch_begin: Optional[Any] = ..., on_epoch_end: Optional[Any] = ..., on_batch_begin: Optional[Any] = ..., on_batch_end: Optional[Any] = ..., on_train_begin: Optional[Any] = ..., on_train_end: Optional[Any] = ..., **kwargs: Any) -> None: ...
