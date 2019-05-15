# Stubs for tensorflow.python.training.server_lib (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.protobuf import cluster_pb2 as cluster_pb2, tensorflow_server_pb2 as tensorflow_server_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.framework import errors as errors
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class Server:
    def __init__(self, server_or_cluster_def: Any, job_name: Optional[Any] = ..., task_index: Optional[Any] = ..., protocol: Optional[Any] = ..., config: Optional[Any] = ..., start: bool = ...) -> None: ...
    def start(self) -> None: ...
    def join(self) -> None: ...
    @property
    def server_def(self): ...
    @property
    def target(self): ...
    @staticmethod
    def create_local_server(config: Optional[Any] = ..., start: bool = ...): ...

class ClusterSpec:
    def __init__(self, cluster: Any) -> None: ...
    def __nonzero__(self): ...
    __bool__: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def as_dict(self): ...
    def as_cluster_def(self): ...
    @property
    def jobs(self): ...
    def num_tasks(self, job_name: Any): ...
    def task_indices(self, job_name: Any): ...
    def task_address(self, job_name: Any, task_index: Any): ...
    def job_tasks(self, job_name: Any): ...
