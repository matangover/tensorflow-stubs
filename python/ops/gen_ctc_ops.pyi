# Stubs for tensorflow.python.ops.gen_ctc_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple as namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

# _CTCBeamSearchDecoderOutput = namedtuple('CTCBeamSearchDecoder', <ERROR>)

def ctc_beam_search_decoder(inputs: Any, sequence_length: Any, beam_width: Any, top_paths: Any, merge_repeated: bool = ..., name: Optional[Any] = ...): ...
def ctc_beam_search_decoder_eager_fallback(inputs: Any, sequence_length: Any, beam_width: Any, top_paths: Any, merge_repeated: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _CTCGreedyDecoderOutput = namedtuple('CTCGreedyDecoder', <ERROR>)

def ctc_greedy_decoder(inputs: Any, sequence_length: Any, merge_repeated: bool = ..., name: Optional[Any] = ...): ...
def ctc_greedy_decoder_eager_fallback(inputs: Any, sequence_length: Any, merge_repeated: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...

# _CTCLossOutput = namedtuple('CTCLoss', <ERROR>)

def ctc_loss(inputs: Any, labels_indices: Any, labels_values: Any, sequence_length: Any, preprocess_collapse_repeated: bool = ..., ctc_merge_repeated: bool = ..., ignore_longer_outputs_than_inputs: bool = ..., name: Optional[Any] = ...): ...
def ctc_loss_eager_fallback(inputs: Any, labels_indices: Any, labels_values: Any, sequence_length: Any, preprocess_collapse_repeated: bool = ..., ctc_merge_repeated: bool = ..., ignore_longer_outputs_than_inputs: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
