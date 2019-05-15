# Stubs for tensorflow.python.training.checkpointable.util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc as abc
import collections as collections
from tensorflow.core.protobuf import checkpointable_object_graph_pb2 as checkpointable_object_graph_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.client import session as session_lib
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.training import checkpoint_management as checkpoint_management
from tensorflow.python.training.checkpointable import base as base, data_structures as data_structures, tracking as tracking
from tensorflow.python.util import deprecation as deprecation, tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

class _CheckpointRestoreCoordinator:
    builder: Any = ...
    object_graph_proto: Any = ...
    restore_uid: Any = ...
    unused_attributes: Any = ...
    object_by_proto_id: Any = ...
    all_python_objects: Any = ...
    save_path_tensor: Any = ...
    save_path_string: Any = ...
    dtype_map: Any = ...
    restore_ops: Any = ...
    restore_ops_by_name: Any = ...
    saveable_object_cache: Any = ...
    new_restore_ops_callback: Any = ...
    deferred_slot_restorations: Any = ...
    slot_restorations: Any = ...
    def __init__(self, object_graph_proto: Any, save_path: Any, save_path_tensor: Any, restore_op_cache: Any, saveable_object_cache: Any) -> None: ...
    def new_restore_ops(self, new_ops: Any) -> None: ...

class _NameBasedRestoreCoordinator:
    save_path: Any = ...
    dtype_map: Any = ...
    unused_attributes: Any = ...
    restore_uid: Any = ...
    def __init__(self, save_path: Any, dtype_map: Optional[Any] = ...) -> None: ...
    def globally_named_object_attributes(self, checkpointable: Any) -> None: ...
    def eager_restore(self, checkpointable: Any) -> None: ...

def add_variable(checkpointable: Any, name: Any, shape: Optional[Any] = ..., dtype: Any = ..., initializer: Optional[Any] = ...): ...
def object_metadata(save_path: Any): ...

class _ObjectIdentityWrapper:
    def __init__(self, wrapped: Any) -> None: ...
    @property
    def unwrapped(self): ...
    def __eq__(self, other: Any): ...
    def __hash__(self): ...

class _WeakObjectIdentityWrapper(_ObjectIdentityWrapper):
    def __init__(self, wrapped: Any) -> None: ...
    @property
    def unwrapped(self): ...

class _ObjectIdentityDictionary(collections.MutableMapping):
    def __init__(self) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> None: ...

class _ObjectIdentityWeakKeyDictionary(_ObjectIdentityDictionary):
    def __len__(self): ...
    def __iter__(self) -> None: ...

class _ObjectIdentitySet(collections.MutableSet):
    def __init__(self, *args: Any) -> None: ...
    def __contains__(self, key: Any): ...
    def discard(self, key: Any) -> None: ...
    def add(self, key: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> None: ...

class _ObjectIdentityWeakSet(_ObjectIdentitySet):
    def __len__(self): ...
    def __iter__(self) -> None: ...

def named_saveables(root_checkpointable: Any): ...
def list_objects(root_checkpointable: Any): ...
def gather_initializers(root_checkpointable: Any): ...
def capture_dependencies(template: Any): ...

class _LoadStatus(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def assert_consumed(self) -> Any: ...
    @abc.abstractmethod
    def assert_existing_objects_matched(self) -> Any: ...
    @abc.abstractmethod
    def run_restore_ops(self, session: Optional[Any] = ...) -> Any: ...
    @abc.abstractmethod
    def initialize_or_restore(self, session: Optional[Any] = ...) -> Any: ...

def streaming_restore(status: Any, session: Optional[Any] = ...): ...

class CheckpointLoadStatus(_LoadStatus):
    def __init__(self, checkpoint: Any, feed_dict: Any, root_checkpointable: Any) -> None: ...
    def assert_consumed(self): ...
    def assert_existing_objects_matched(self): ...
    def run_restore_ops(self, session: Optional[Any] = ...) -> None: ...
    def initialize_or_restore(self, session: Optional[Any] = ...) -> None: ...

class InitializationOnlyStatus(_LoadStatus):
    def __init__(self, root_checkpointable: Any, restore_uid: Any) -> None: ...
    def assert_consumed(self) -> None: ...
    def assert_existing_objects_matched(self) -> None: ...
    def run_restore_ops(self, session: Optional[Any] = ...) -> None: ...
    def initialize_or_restore(self, session: Optional[Any] = ...) -> None: ...

class NameBasedSaverStatus(_LoadStatus):
    def __init__(self, checkpoint: Any, root_checkpointable: Any) -> None: ...
    def assert_consumed(self): ...
    def assert_existing_objects_matched(self): ...
    def run_restore_ops(self, session: Optional[Any] = ...) -> None: ...
    def initialize_or_restore(self, session: Optional[Any] = ...) -> None: ...

class _SessionWithFeedDictAdditions(session_lib.SessionInterface):
    def __init__(self, session: Any, feed_additions: Any) -> None: ...
    def run(self, fetches: Any, feed_dict: Optional[Any] = ..., **kwargs: Any): ...

class CheckpointableSaver:
    def __init__(self, root_checkpointable: Any) -> None: ...
    def freeze(self): ...
    def save(self, file_prefix: Any, checkpoint_number: Optional[Any] = ..., session: Optional[Any] = ...): ...
    def restore(self, save_path: Any): ...

def frozen_saver(root_checkpointable: Any): ...

class Checkpoint(tracking.Checkpointable):
    def __init__(self, **kwargs: Any) -> None: ...
    def write(self, file_prefix: Any, session: Optional[Any] = ...): ...
    @property
    def save_counter(self): ...
    def save(self, file_prefix: Any, session: Optional[Any] = ...): ...
    def restore(self, save_path: Any): ...