# Stubs for tensorflow.contrib.factorization.python.ops.gmm (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib import framework as framework
from tensorflow.contrib.factorization.python.ops import gmm_ops as gmm_ops
from tensorflow.contrib.framework.python.framework import checkpoint_utils as checkpoint_utils
from tensorflow.contrib.learn.python.learn.estimators import estimator as estimator
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import array_ops as array_ops, state_ops as state_ops
from tensorflow.python.ops.control_flow_ops import with_dependencies as with_dependencies
from tensorflow.python.training import session_run_hook as session_run_hook, training_util as training_util
from typing import Any as Any, Optional as Optional

class _InitializeClustersHook(session_run_hook.SessionRunHook):
    def __init__(self, init_op: Any, is_initialized_op: Any, is_chief: Any) -> None: ...
    def after_create_session(self, session: Any, _: Any) -> None: ...

class GMM(estimator.Estimator):
    SCORES: str = ...
    LOG_LIKELIHOOD: str = ...
    ASSIGNMENTS: str = ...
    def __init__(self, num_clusters: Any, model_dir: Optional[Any] = ..., random_seed: int = ..., params: str = ..., initial_clusters: str = ..., covariance_type: str = ..., config: Optional[Any] = ...) -> None: ...
    def predict_assignments(self, input_fn: Optional[Any] = ..., batch_size: Optional[Any] = ..., outputs: Optional[Any] = ...) -> None: ...
    def score(self, input_fn: Optional[Any] = ..., batch_size: Optional[Any] = ..., steps: Optional[Any] = ...): ...
    def weights(self): ...
    def clusters(self): ...
    def covariances(self): ...