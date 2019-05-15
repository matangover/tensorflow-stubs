# Stubs for tensorflow.python.grappler.cluster (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.framework import step_stats_pb2 as step_stats_pb2
from tensorflow.core.grappler.costs import op_performance_data_pb2 as op_performance_data_pb2
from tensorflow.core.protobuf import device_properties_pb2 as device_properties_pb2
from tensorflow.python.framework import errors as errors
from typing import Any as Any, Optional as Optional

class Cluster:
    def __init__(self, allow_soft_placement: bool = ..., disable_detailed_stats: bool = ..., disable_timeline: bool = ..., devices: Optional[Any] = ...) -> None: ...
    def Shutdown(self) -> None: ...
    def __del__(self) -> None: ...
    @property
    def tf_cluster(self): ...
    def ListDevices(self): ...
    def ListAvailableOps(self): ...
    def GetSupportedDevices(self, item: Any): ...
    def EstimatePerformance(self, device: Any): ...
    def MeasureCosts(self, item: Any): ...
    def DeterminePeakMemoryUsage(self, item: Any): ...

def Provision(allow_soft_placement: bool = ..., disable_detailed_stats: bool = ..., disable_timeline: bool = ..., devices: Optional[Any] = ...) -> None: ...
