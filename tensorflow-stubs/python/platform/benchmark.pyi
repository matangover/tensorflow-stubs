# Stubs for tensorflow.python.platform.benchmark (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.core.util import test_log_pb2 as test_log_pb2
from tensorflow.python.client import timeline as timeline
from tensorflow.python.platform import app as app, gfile as gfile
from tensorflow.python.util import tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

GLOBAL_BENCHMARK_REGISTRY: Any
TEST_REPORTER_TEST_ENV: str

class _BenchmarkRegistrar(type):
    def __new__(mcs: Any, clsname: Any, base: Any, attrs: Any): ...

class Benchmark(metaclass=_BenchmarkRegistrar):
    @classmethod
    def is_abstract(cls): ...
    def report_benchmark(self, iters: Optional[Any] = ..., cpu_time: Optional[Any] = ..., wall_time: Optional[Any] = ..., throughput: Optional[Any] = ..., extras: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...

class TensorFlowBenchmark(Benchmark):
    @classmethod
    def is_abstract(cls): ...
    def run_op_benchmark(self, sess: Any, op_or_tensor: Any, feed_dict: Optional[Any] = ..., burn_iters: int = ..., min_iters: int = ..., store_trace: bool = ..., store_memory_usage: bool = ..., name: Optional[Any] = ..., extras: Optional[Any] = ..., mbs: int = ...): ...

def benchmarks_main(true_main: Any, argv: Optional[Any] = ...): ...
