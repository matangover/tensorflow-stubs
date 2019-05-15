# Stubs for tensorflow.contrib.distributions.python.ops.bijectors.conditional_bijector (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.ops.distributions import bijector as bijector
from typing import Any as Any

class ConditionalBijector(bijector.Bijector):
    def forward(self, x: Any, name: str = ..., **condition_kwargs: Any): ...
    def inverse(self, y: Any, name: str = ..., **condition_kwargs: Any): ...
    def inverse_log_det_jacobian(self, y: Any, event_ndims: Any, name: str = ..., **condition_kwargs: Any): ...
    def forward_log_det_jacobian(self, x: Any, event_ndims: Any, name: str = ..., **condition_kwargs: Any): ...