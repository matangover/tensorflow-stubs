# Stubs for tensorflow.contrib.learn.python.learn.estimators.estimator (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from collections import namedtuple as namedtuple
from tensorflow.contrib import layers as layers
from tensorflow.contrib.framework import deprecated as deprecated, deprecated_args as deprecated_args, list_variables as list_variables, load_variable as load_variable
from tensorflow.contrib.learn.python.learn import evaluable as evaluable, metric_spec as metric_spec, trainable as trainable
from tensorflow.contrib.learn.python.learn.estimators import _sklearn as sklearn, constants as constants, metric_key as metric_key, run_config as run_config, tensor_signature as tensor_signature
from tensorflow.contrib.learn.python.learn.estimators._sklearn import NotFittedError as NotFittedError
from tensorflow.contrib.learn.python.learn.learn_io import data_feeder as data_feeder
from tensorflow.contrib.learn.python.learn.utils import export as export, saved_model_export_utils as saved_model_export_utils
from tensorflow.contrib.meta_graph_transform import meta_graph_transform as meta_graph_transform
from tensorflow.contrib.training.python.training import evaluation as evaluation
from tensorflow.core.framework import summary_pb2 as summary_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.framework import ops as ops, random_seed as random_seed, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import control_flow_ops as control_flow_ops, lookup_ops as lookup_ops, resources as resources, variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import tag_constants as tag_constants
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, checkpoint_management as checkpoint_management, device_setter as device_setter, monitored_session as monitored_session, saver as saver, training_util as training_util
from tensorflow.python.util import compat as compat, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from typing import Any as Any, Optional as Optional

AS_ITERABLE_DATE: str
AS_ITERABLE_INSTRUCTIONS: str
SCIKIT_DECOUPLE_DATE: str
SCIKIT_DECOUPLE_INSTRUCTIONS: str

def infer_real_valued_columns_from_input_fn(input_fn: Any): ...
def infer_real_valued_columns_from_input(x: Any): ...

GraphRewriteSpec = namedtuple('GraphRewriteSpec', ['tags', 'transforms'])

class BaseEstimator(sklearn.BaseEstimator, evaluable.Evaluable, trainable.Trainable, metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    def __init__(self, model_dir: Optional[Any] = ..., config: Optional[Any] = ...) -> None: ...
    @property
    def config(self): ...
    @property
    def model_fn(self): ...
    def fit(self, x: Optional[Any] = ..., y: Optional[Any] = ..., input_fn: Optional[Any] = ..., steps: Optional[Any] = ..., batch_size: Optional[Any] = ..., monitors: Optional[Any] = ..., max_steps: Optional[Any] = ...): ...
    def partial_fit(self, x: Optional[Any] = ..., y: Optional[Any] = ..., input_fn: Optional[Any] = ..., steps: int = ..., batch_size: Optional[Any] = ..., monitors: Optional[Any] = ...): ...
    def evaluate(self, x: Optional[Any] = ..., y: Optional[Any] = ..., input_fn: Optional[Any] = ..., feed_fn: Optional[Any] = ..., batch_size: Optional[Any] = ..., steps: Optional[Any] = ..., metrics: Optional[Any] = ..., name: Optional[Any] = ..., checkpoint_path: Optional[Any] = ..., hooks: Optional[Any] = ..., log_progress: bool = ...): ...
    def predict(self, x: Optional[Any] = ..., input_fn: Optional[Any] = ..., batch_size: Optional[Any] = ..., outputs: Optional[Any] = ..., as_iterable: bool = ..., iterate_batches: bool = ...): ...
    def get_variable_value(self, name: Any): ...
    def get_variable_names(self): ...
    @property
    def model_dir(self): ...
    def export(self, export_dir: Any, input_fn: Any = ..., input_feature_key: Optional[Any] = ..., use_deprecated_input_fn: bool = ..., signature_fn: Optional[Any] = ..., prediction_key: Optional[Any] = ..., default_batch_size: int = ..., exports_to_keep: Optional[Any] = ..., checkpoint_path: Optional[Any] = ...): ...

class Estimator(BaseEstimator):
    params: Any = ...
    def __init__(self, model_fn: Optional[Any] = ..., model_dir: Optional[Any] = ..., config: Optional[Any] = ..., params: Optional[Any] = ..., feature_engineering_fn: Optional[Any] = ...) -> None: ...
    def export_savedmodel(self, export_dir_base: Any, serving_input_fn: Any, default_output_alternative_key: Optional[Any] = ..., assets_extra: Optional[Any] = ..., as_text: bool = ..., checkpoint_path: Optional[Any] = ..., graph_rewrite_specs: Any = ..., strip_default_attrs: bool = ...): ...

class SKCompat(sklearn.BaseEstimator):
    def __init__(self, estimator: Any) -> None: ...
    def fit(self, x: Any, y: Any, batch_size: int = ..., steps: Optional[Any] = ..., max_steps: Optional[Any] = ..., monitors: Optional[Any] = ...): ...
    def score(self, x: Any, y: Any, batch_size: int = ..., steps: Optional[Any] = ..., metrics: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def predict(self, x: Any, batch_size: int = ..., outputs: Optional[Any] = ...): ...
