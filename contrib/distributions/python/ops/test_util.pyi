# Stubs for tensorflow.contrib.distributions.python.ops.test_util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, histogram_ops as histogram_ops, linalg_ops as linalg_ops, math_ops as math_ops
from typing import Any as Any, Optional as Optional

class DiscreteScalarDistributionTestHelpers:
    def run_test_sample_consistent_log_prob(self, sess_run_fn: Any, dist: Any, num_samples: Any = ..., num_threshold: Any = ..., seed: int = ..., batch_size: Optional[Any] = ..., rtol: float = ..., atol: float = ...) -> None: ...
    def run_test_sample_consistent_mean_variance(self, sess_run_fn: Any, dist: Any, num_samples: Any = ..., seed: int = ..., rtol: float = ..., atol: float = ...) -> None: ...
    def histogram(self, x: Any, value_range: Optional[Any] = ..., nbins: Optional[Any] = ..., name: Optional[Any] = ...): ...

class VectorDistributionTestHelpers:
    def run_test_sample_consistent_log_prob(self, sess_run_fn: Any, dist: Any, num_samples: Any = ..., radius: float = ..., center: float = ..., seed: int = ..., rtol: float = ..., atol: float = ...): ...
    def run_test_sample_consistent_mean_covariance(self, sess_run_fn: Any, dist: Any, num_samples: Any = ..., seed: int = ..., rtol: float = ..., atol: float = ..., cov_rtol: Optional[Any] = ..., cov_atol: Optional[Any] = ...) -> None: ...