# Stubs for tensorflow.contrib.cluster_resolver.python.training.gce_cluster_resolver (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.cluster_resolver.python.training.cluster_resolver import ClusterResolver as ClusterResolver
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from typing import Any as Any, Optional as Optional

class GceClusterResolver(ClusterResolver):
    def __init__(self, project: Any, zone: Any, instance_group: Any, port: Any, job_name: str = ..., credentials: str = ..., service: Optional[Any] = ...) -> None: ...
    def cluster_spec(self): ...
    def master(self): ...
