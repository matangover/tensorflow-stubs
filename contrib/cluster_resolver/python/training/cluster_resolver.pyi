# Stubs for tensorflow.contrib.cluster_resolver.python.training.cluster_resolver (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from typing import Any as Any

class ClusterResolver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cluster_spec(self) -> Any: ...
    @abc.abstractmethod
    def master(self) -> Any: ...

class SimpleClusterResolver(ClusterResolver):
    def __init__(self, cluster_spec: Any, master: str = ...) -> None: ...
    def cluster_spec(self): ...
    def master(self): ...

class UnionClusterResolver(ClusterResolver):
    def __init__(self, *args: Any) -> None: ...
    def cluster_spec(self): ...
    def master(self): ...