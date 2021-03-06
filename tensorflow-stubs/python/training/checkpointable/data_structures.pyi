# Stubs for tensorflow.python.training.checkpointable.data_structures (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import collections as collections
from tensorflow.python.ops import variables as variables
from tensorflow.python.training.checkpointable import base as base, layer_utils as layer_utils
from typing import Any as Any

class NoDependency:
    value: Any = ...
    def __init__(self, value: Any) -> None: ...

def sticky_attribute_assignment(checkpointable: Any, name: Any, value: Any): ...

class CheckpointableDataStructure(base.CheckpointableBase):
    trainable: bool = ...
    def __init__(self) -> None: ...
    @property
    def layers(self): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def weights(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def variables(self): ...
    @property
    def updates(self): ...
    @property
    def losses(self): ...
    def __hash__(self): ...
    def __eq__(self, other: Any): ...

class List(CheckpointableDataStructure, collections.Sequence):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    def append(self, value: Any) -> None: ...
    def extend(self, values: Any) -> None: ...
    def __iadd__(self, values: Any): ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __getitem__(self, key: Any): ...
    def __len__(self): ...

class _ListWrapper(list, collections.MutableSequence):
    def __init__(self, wrapped_list: Any) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def append(self, value: Any) -> None: ...
    def extend(self, values: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def __hash__(self) -> None: ...
    def insert(self, index: Any, obj: Any) -> None: ...

class Mapping(CheckpointableDataStructure, collections.Mapping):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __len__(self): ...
    def __iter__(self): ...

class _DictWrapper(Mapping, collections.MutableMapping):
    def __new__(cls, *args: Any): ...
    def __init__(self, wrapped_dict: Any) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __hash__(self) -> None: ...
    def __eq__(self, other: Any): ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
