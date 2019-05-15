# Stubs for tensorflow.contrib.factorization.python.ops.kmeans (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.factorization.python.ops import clustering_ops as clustering_ops
from tensorflow.python.estimator import estimator as estimator
from tensorflow.python.estimator.export import export_output as export_output
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, metrics as metrics, state_ops as state_ops
from tensorflow.python.saved_model import signature_constants as signature_constants
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import session_run_hook as session_run_hook, training_util as training_util
from typing import Any as Any, Optional as Optional

class _LossRelativeChangeHook(session_run_hook.SessionRunHook):
    def __init__(self, loss_tensor: Any, tolerance: Any) -> None: ...
    def before_run(self, run_context: Any): ...
    def after_run(self, run_context: Any, run_values: Any) -> None: ...

class _InitializeClustersHook(session_run_hook.SessionRunHook):
    def __init__(self, init_op: Any, is_initialized_var: Any, is_chief: Any) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...

class _ModelFn:
    def __init__(self, num_clusters: Any, initial_clusters: Any, distance_metric: Any, random_seed: Any, use_mini_batch: Any, mini_batch_steps_per_iteration: Any, kmeans_plus_plus_num_retries: Any, relative_tolerance: Any, feature_columns: Any) -> None: ...
    def model_fn(self, features: Any, mode: Any, config: Any): ...

class KMeansClustering(estimator.Estimator):
    SQUARED_EUCLIDEAN_DISTANCE: Any = ...
    COSINE_DISTANCE: Any = ...
    RANDOM_INIT: Any = ...
    KMEANS_PLUS_PLUS_INIT: Any = ...
    SCORE: str = ...
    CLUSTER_INDEX: str = ...
    ALL_DISTANCES: str = ...
    CLUSTER_CENTERS_VAR_NAME: Any = ...
    def __init__(self, num_clusters: Any, model_dir: Optional[Any] = ..., initial_clusters: Any = ..., distance_metric: Any = ..., random_seed: int = ..., use_mini_batch: bool = ..., mini_batch_steps_per_iteration: int = ..., kmeans_plus_plus_num_retries: int = ..., relative_tolerance: Optional[Any] = ..., config: Optional[Any] = ..., feature_columns: Optional[Any] = ...) -> None: ...
    def predict_cluster_index(self, input_fn: Any) -> None: ...
    def score(self, input_fn: Any): ...
    def transform(self, input_fn: Any) -> None: ...
    def cluster_centers(self): ...
