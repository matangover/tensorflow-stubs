# Stubs for tensorflow.contrib.boosted_trees.estimator_batch.dnn_tree_combined_estimator (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib import layers as layers
from tensorflow.contrib.boosted_trees.estimator_batch import distillation_loss as distillation_loss, estimator_utils as estimator_utils, model as model, trainer_hooks as trainer_hooks
from tensorflow.contrib.boosted_trees.python.ops import model_ops as model_ops
from tensorflow.contrib.boosted_trees.python.training.functions import gbdt_batch as gbdt_batch
from tensorflow.contrib.layers.python.layers import optimizers as optimizers
from tensorflow.contrib.learn.python.learn.estimators import estimator as estimator, model_fn as model_fn
from tensorflow.python.estimator import estimator as core_estimator
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, nn as nn, partitioned_variables as partitioned_variables, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.summary import summary as summary
from tensorflow.python.training import training_util as training_util
from typing import Any as Any, Optional as Optional

class DNNBoostedTreeCombinedClassifier(estimator.Estimator):
    def __init__(self, dnn_hidden_units: Any, dnn_feature_columns: Any, tree_learner_config: Any, num_trees: Any, tree_examples_per_layer: Any, n_classes: int = ..., weight_column_name: Optional[Any] = ..., model_dir: Optional[Any] = ..., config: Optional[Any] = ..., label_name: Optional[Any] = ..., label_keys: Optional[Any] = ..., feature_engineering_fn: Optional[Any] = ..., dnn_optimizer: str = ..., dnn_activation_fn: Any = ..., dnn_dropout: Optional[Any] = ..., dnn_input_layer_partitioner: Optional[Any] = ..., dnn_input_layer_to_tree: bool = ..., dnn_steps_to_train: int = ..., predict_with_tree_only: bool = ..., tree_feature_columns: Optional[Any] = ..., tree_center_bias: bool = ..., dnn_to_tree_distillation_param: Optional[Any] = ..., use_core_versions: bool = ..., override_global_step_value: Optional[Any] = ...) -> None: ...

class DNNBoostedTreeCombinedRegressor(estimator.Estimator):
    def __init__(self, dnn_hidden_units: Any, dnn_feature_columns: Any, tree_learner_config: Any, num_trees: Any, tree_examples_per_layer: Any, weight_column_name: Optional[Any] = ..., model_dir: Optional[Any] = ..., config: Optional[Any] = ..., label_name: Optional[Any] = ..., label_dimension: int = ..., feature_engineering_fn: Optional[Any] = ..., dnn_optimizer: str = ..., dnn_activation_fn: Any = ..., dnn_dropout: Optional[Any] = ..., dnn_input_layer_partitioner: Optional[Any] = ..., dnn_input_layer_to_tree: bool = ..., dnn_steps_to_train: int = ..., predict_with_tree_only: bool = ..., tree_feature_columns: Optional[Any] = ..., tree_center_bias: bool = ..., dnn_to_tree_distillation_param: Optional[Any] = ..., use_core_versions: bool = ..., override_global_step_value: Optional[Any] = ...) -> None: ...

class DNNBoostedTreeCombinedEstimator(estimator.Estimator):
    def __init__(self, dnn_hidden_units: Any, dnn_feature_columns: Any, tree_learner_config: Any, num_trees: Any, tree_examples_per_layer: Any, head: Any, model_dir: Optional[Any] = ..., config: Optional[Any] = ..., feature_engineering_fn: Optional[Any] = ..., dnn_optimizer: str = ..., dnn_activation_fn: Any = ..., dnn_dropout: Optional[Any] = ..., dnn_input_layer_partitioner: Optional[Any] = ..., dnn_input_layer_to_tree: bool = ..., dnn_steps_to_train: int = ..., predict_with_tree_only: bool = ..., tree_feature_columns: Optional[Any] = ..., tree_center_bias: bool = ..., dnn_to_tree_distillation_param: Optional[Any] = ..., use_core_versions: bool = ..., override_global_step_value: Optional[Any] = ...) -> None: ...

class CoreDNNBoostedTreeCombinedEstimator(core_estimator.Estimator):
    def __init__(self, dnn_hidden_units: Any, dnn_feature_columns: Any, tree_learner_config: Any, num_trees: Any, tree_examples_per_layer: Any, head: Any, model_dir: Optional[Any] = ..., config: Optional[Any] = ..., dnn_optimizer: str = ..., dnn_activation_fn: Any = ..., dnn_dropout: Optional[Any] = ..., dnn_input_layer_partitioner: Optional[Any] = ..., dnn_input_layer_to_tree: bool = ..., dnn_steps_to_train: int = ..., predict_with_tree_only: bool = ..., tree_feature_columns: Optional[Any] = ..., tree_center_bias: bool = ..., dnn_to_tree_distillation_param: Optional[Any] = ...) -> None: ...