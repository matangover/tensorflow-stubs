# Stubs for tensorflow.contrib.factorization.python.ops.gen_clustering_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def kmc2_chain_initialization(distances: Any, seed: Any, name: Optional[Any] = ...): ...
def kmc2_chain_initialization_eager_fallback(distances: Any, seed: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def kmeans_plus_plus_initialization(points: Any, num_to_sample: Any, seed: Any, num_retries_per_sample: Any, name: Optional[Any] = ...): ...
def kmeans_plus_plus_initialization_eager_fallback(points: Any, num_to_sample: Any, seed: Any, num_retries_per_sample: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _NearestNeighborsOutput = namedtuple('NearestNeighbors', <ERROR>)

def nearest_neighbors(points: Any, centers: Any, k: Any, name: Optional[Any] = ...): ...
def nearest_neighbors_eager_fallback(points: Any, centers: Any, k: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
