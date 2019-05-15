# Stubs for tensorflow.contrib.losses.python.metric_learning.metric_loss_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, logging_ops as logging_ops, math_ops as math_ops, nn as nn, script_ops as script_ops, sparse_ops as sparse_ops
from tensorflow.python.summary import summary as summary
from typing import Any as Any

HAS_SKLEARN: bool

def pairwise_distance(feature: Any, squared: bool = ...): ...
def contrastive_loss(labels: Any, embeddings_anchor: Any, embeddings_positive: Any, margin: float = ...): ...
def masked_maximum(data: Any, mask: Any, dim: int = ...): ...
def masked_minimum(data: Any, mask: Any, dim: int = ...): ...
def triplet_semihard_loss(labels: Any, embeddings: Any, margin: float = ...): ...
def npairs_loss(labels: Any, embeddings_anchor: Any, embeddings_positive: Any, reg_lambda: float = ..., print_losses: bool = ...): ...
def npairs_loss_multilabel(sparse_labels: Any, embeddings_anchor: Any, embeddings_positive: Any, reg_lambda: float = ..., print_losses: bool = ...): ...
def lifted_struct_loss(labels: Any, embeddings: Any, margin: float = ...): ...
def update_1d_tensor(y: Any, index: Any, value: Any): ...
def get_cluster_assignment(pairwise_distances: Any, centroid_ids: Any): ...
def compute_facility_energy(pairwise_distances: Any, centroid_ids: Any): ...
def compute_clustering_score(labels: Any, predictions: Any, margin_type: Any): ...
def compute_augmented_facility_locations(pairwise_distances: Any, labels: Any, all_ids: Any, margin_multiplier: Any, margin_type: Any): ...
def update_medoid_per_cluster(pairwise_distances: Any, pairwise_distances_subset: Any, labels: Any, chosen_ids: Any, cluster_member_ids: Any, cluster_idx: Any, margin_multiplier: Any, margin_type: Any): ...
def update_all_medoids(pairwise_distances: Any, predictions: Any, labels: Any, chosen_ids: Any, margin_multiplier: Any, margin_type: Any): ...
def compute_augmented_facility_locations_pam(pairwise_distances: Any, labels: Any, margin_multiplier: Any, margin_type: Any, chosen_ids: Any, pam_max_iter: int = ...): ...
def compute_gt_cluster_score(pairwise_distances: Any, labels: Any): ...
def cluster_loss(labels: Any, embeddings: Any, margin_multiplier: Any, enable_pam_finetuning: bool = ..., margin_type: str = ..., print_losses: bool = ...): ...