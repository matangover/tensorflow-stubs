# Stubs for tensorflow.contrib.legacy_seq2seq.python.ops.seq2seq (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.rnn.python.ops import core_rnn_cell as core_rnn_cell
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, embedding_ops as embedding_ops, math_ops as math_ops, nn_ops as nn_ops, rnn as rnn, rnn_cell_impl as rnn_cell_impl, variable_scope as variable_scope
from tensorflow.python.util import nest as nest
from typing import Any as Any, Optional as Optional

Linear: Any

def rnn_decoder(decoder_inputs: Any, initial_state: Any, cell: Any, loop_function: Optional[Any] = ..., scope: Optional[Any] = ...): ...
def basic_rnn_seq2seq(encoder_inputs: Any, decoder_inputs: Any, cell: Any, dtype: Any = ..., scope: Optional[Any] = ...): ...
def tied_rnn_seq2seq(encoder_inputs: Any, decoder_inputs: Any, cell: Any, loop_function: Optional[Any] = ..., dtype: Any = ..., scope: Optional[Any] = ...): ...
def embedding_rnn_decoder(decoder_inputs: Any, initial_state: Any, cell: Any, num_symbols: Any, embedding_size: Any, output_projection: Optional[Any] = ..., feed_previous: bool = ..., update_embedding_for_previous: bool = ..., scope: Optional[Any] = ...): ...
def embedding_rnn_seq2seq(encoder_inputs: Any, decoder_inputs: Any, cell: Any, num_encoder_symbols: Any, num_decoder_symbols: Any, embedding_size: Any, output_projection: Optional[Any] = ..., feed_previous: bool = ..., dtype: Optional[Any] = ..., scope: Optional[Any] = ...): ...
def embedding_tied_rnn_seq2seq(encoder_inputs: Any, decoder_inputs: Any, cell: Any, num_symbols: Any, embedding_size: Any, num_decoder_symbols: Optional[Any] = ..., output_projection: Optional[Any] = ..., feed_previous: bool = ..., dtype: Optional[Any] = ..., scope: Optional[Any] = ...): ...
def attention_decoder(decoder_inputs: Any, initial_state: Any, attention_states: Any, cell: Any, output_size: Optional[Any] = ..., num_heads: int = ..., loop_function: Optional[Any] = ..., dtype: Optional[Any] = ..., scope: Optional[Any] = ..., initial_state_attention: bool = ...): ...
def embedding_attention_decoder(decoder_inputs: Any, initial_state: Any, attention_states: Any, cell: Any, num_symbols: Any, embedding_size: Any, num_heads: int = ..., output_size: Optional[Any] = ..., output_projection: Optional[Any] = ..., feed_previous: bool = ..., update_embedding_for_previous: bool = ..., dtype: Optional[Any] = ..., scope: Optional[Any] = ..., initial_state_attention: bool = ...): ...
def embedding_attention_seq2seq(encoder_inputs: Any, decoder_inputs: Any, cell: Any, num_encoder_symbols: Any, num_decoder_symbols: Any, embedding_size: Any, num_heads: int = ..., output_projection: Optional[Any] = ..., feed_previous: bool = ..., dtype: Optional[Any] = ..., scope: Optional[Any] = ..., initial_state_attention: bool = ...): ...
def one2many_rnn_seq2seq(encoder_inputs: Any, decoder_inputs_dict: Any, enc_cell: Any, dec_cells_dict: Any, num_encoder_symbols: Any, num_decoder_symbols_dict: Any, embedding_size: Any, feed_previous: bool = ..., dtype: Optional[Any] = ..., scope: Optional[Any] = ...): ...
def sequence_loss_by_example(logits: Any, targets: Any, weights: Any, average_across_timesteps: bool = ..., softmax_loss_function: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sequence_loss(logits: Any, targets: Any, weights: Any, average_across_timesteps: bool = ..., average_across_batch: bool = ..., softmax_loss_function: Optional[Any] = ..., name: Optional[Any] = ...): ...
def model_with_buckets(encoder_inputs: Any, decoder_inputs: Any, targets: Any, weights: Any, buckets: Any, seq2seq: Any, softmax_loss_function: Optional[Any] = ..., per_example_loss: bool = ..., name: Optional[Any] = ...): ...
