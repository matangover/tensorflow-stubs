# Stubs for tensorflow.contrib.tensor_forest.python.tensor_forest (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.tensor_forest.python.ops import data_ops as data_ops, model_ops as model_ops, stats_ops as stats_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, random_ops as random_ops, variable_scope as variable_scope
from typing import Any as Any, Optional as Optional

CLASSIFICATION_LEAF_MODEL_TYPES: Any
REGRESSION_MODEL_TYPE: Any
FINISH_TYPES: Any
PRUNING_TYPES: Any
SPLIT_TYPES: Any

def parse_number_or_string_to_proto(proto: Any, param: Any) -> None: ...
def build_params_proto(params: Any): ...

class ForestHParams:
    num_trees: Any = ...
    max_nodes: Any = ...
    bagging_fraction: Any = ...
    feature_bagging_fraction: Any = ...
    num_splits_to_consider: Any = ...
    max_fertile_nodes: Any = ...
    split_after_samples: Any = ...
    valid_leaf_threshold: Any = ...
    dominate_method: Any = ...
    dominate_fraction: Any = ...
    model_name: Any = ...
    split_finish_name: Any = ...
    split_pruning_name: Any = ...
    collate_examples: Any = ...
    checkpoint_stats: Any = ...
    use_running_stats_method: Any = ...
    initialize_average_splits: Any = ...
    inference_tree_paths: Any = ...
    param_file: Any = ...
    split_name: Any = ...
    early_finish_check_every_samples: Any = ...
    prune_every_samples: Any = ...
    def __init__(self, num_trees: int = ..., max_nodes: int = ..., bagging_fraction: float = ..., num_splits_to_consider: int = ..., feature_bagging_fraction: float = ..., max_fertile_nodes: int = ..., split_after_samples: int = ..., valid_leaf_threshold: int = ..., dominate_method: str = ..., dominate_fraction: float = ..., model_name: str = ..., split_finish_name: str = ..., split_pruning_name: str = ..., prune_every_samples: int = ..., early_finish_check_every_samples: int = ..., collate_examples: bool = ..., checkpoint_stats: bool = ..., use_running_stats_method: bool = ..., initialize_average_splits: bool = ..., inference_tree_paths: bool = ..., param_file: Optional[Any] = ..., split_name: str = ..., **kwargs: Any) -> None: ...
    def values(self): ...
    bagged_num_features: Any = ...
    bagged_features: Any = ...
    regression: Any = ...
    num_outputs: Any = ...
    num_output_columns: Any = ...
    base_random_seed: Any = ...
    leaf_model_type: Any = ...
    stats_model_type: Any = ...
    finish_type: Any = ...
    pruning_type: Any = ...
    split_type: Any = ...
    def fill(self): ...

def get_epoch_variable(): ...

class TreeVariables:
    stats: Any = ...
    tree: Any = ...
    def __init__(self, params: Any, tree_num: Any, training: Any, tree_config: str = ..., tree_stat: str = ...) -> None: ...
    def get_tree_name(self, name: Any, num: Any): ...

class ForestVariables:
    variables: Any = ...
    device_dummies: Any = ...
    def __init__(self, params: Any, device_assigner: Any, training: bool = ..., tree_variables_class: Any = ..., tree_configs: Optional[Any] = ..., tree_stats: Optional[Any] = ...) -> None: ...
    def __setitem__(self, t: Any, val: Any) -> None: ...
    def __getitem__(self, t: Any): ...

class RandomForestGraphs:
    params: Any = ...
    device_assigner: Any = ...
    variables: Any = ...
    trees: Any = ...
    def __init__(self, params: Any, tree_configs: Optional[Any] = ..., tree_stats: Optional[Any] = ..., device_assigner: Optional[Any] = ..., variables: Optional[Any] = ..., tree_variables_class: Any = ..., tree_graphs: Optional[Any] = ..., training: bool = ...) -> None: ...
    def get_all_resource_handles(self): ...
    def training_graph(self, input_data: Any, input_labels: Any, num_trainers: int = ..., trainer_id: int = ..., **tree_kwargs: Any): ...
    def inference_graph(self, input_data: Any, **inference_args: Any): ...
    def average_size(self): ...
    def training_loss(self, features: Any, labels: Any, name: str = ...): ...
    def validation_loss(self, features: Any, labels: Any): ...
    def average_impurity(self): ...
    def feature_importances(self): ...

class RandomTreeGraphs:
    variables: Any = ...
    params: Any = ...
    tree_num: Any = ...
    def __init__(self, variables: Any, params: Any, tree_num: Any) -> None: ...
    def training_graph(self, input_data: Any, input_labels: Any, random_seed: Any, data_spec: Any, sparse_features: Optional[Any] = ..., input_weights: Optional[Any] = ...): ...
    def inference_graph(self, input_data: Any, data_spec: Any, sparse_features: Optional[Any] = ...): ...
    def size(self): ...
    def feature_usage_counts(self): ...