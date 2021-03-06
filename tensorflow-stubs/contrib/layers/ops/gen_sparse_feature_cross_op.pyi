# Stubs for tensorflow.contrib.layers.ops.gen_sparse_feature_cross_op (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

# _SparseFeatureCrossOutput = namedtuple('SparseFeatureCross', <ERROR>)

def sparse_feature_cross(indices: Any, values: Any, shapes: Any, dense: Any, hashed_output: Any, num_buckets: Any, out_type: Any, internal_type: Any, name: Optional[Any] = ...): ...
def sparse_feature_cross_eager_fallback(indices: Any, values: Any, shapes: Any, dense: Any, hashed_output: Any, num_buckets: Any, out_type: Any, internal_type: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _SparseFeatureCrossV2Output = namedtuple('SparseFeatureCrossV2', <ERROR>)

def sparse_feature_cross_v2(indices: Any, values: Any, shapes: Any, dense: Any, hashed_output: Any, num_buckets: Any, hash_key: Any, out_type: Any, internal_type: Any, name: Optional[Any] = ...): ...
def sparse_feature_cross_v2_eager_fallback(indices: Any, values: Any, shapes: Any, dense: Any, hashed_output: Any, num_buckets: Any, hash_key: Any, out_type: Any, internal_type: Any, name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
