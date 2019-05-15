# Stubs for tensorflow.contrib.eager.python.examples.rnn_ptb.rnn_ptb (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import tensorflow as tf
from tensorflow.contrib.cudnn_rnn.python.layers import cudnn_rnn as cudnn_rnn
from tensorflow.contrib.eager.python import tfe as tfe
from typing import Any as Any

layers: Any

class RNN(tf.keras.Model):
    keep_ratio: Any = ...
    cells: Any = ...
    def __init__(self, hidden_dim: Any, num_layers: Any, keep_ratio: Any) -> None: ...
    def call(self, input_seq: Any, training: Any): ...

class Embedding(layers.Layer):
    vocab_size: Any = ...
    embedding_dim: Any = ...
    def __init__(self, vocab_size: Any, embedding_dim: Any, **kwargs: Any) -> None: ...
    embedding: Any = ...
    def build(self, _: Any) -> None: ...
    def call(self, x: Any): ...

class PTBModel(tf.keras.Model):
    keep_ratio: Any = ...
    use_cudnn_rnn: Any = ...
    embedding: Any = ...
    rnn: Any = ...
    linear: Any = ...
    def __init__(self, vocab_size: Any, embedding_dim: Any, hidden_dim: Any, num_layers: Any, dropout_ratio: Any, use_cudnn_rnn: bool = ...) -> None: ...
    def call(self, input_seq: Any, training: Any): ...

def clip_gradients(grads_and_vars: Any, clip_ratio: Any): ...
def loss_fn(model: Any, inputs: Any, targets: Any, training: Any): ...
def evaluate(model: Any, data: Any): ...
def train(model: Any, optimizer: Any, train_data: Any, sequence_length: Any, clip_ratio: Any): ...

class Datasets:
    word2idx: Any = ...
    idx2word: Any = ...
    train: Any = ...
    valid: Any = ...
    def __init__(self, path: Any) -> None: ...
    def vocab_size(self): ...
    def add(self, word: Any) -> None: ...
    def tokenize(self, path: Any): ...

def small_model(use_cudnn_rnn: Any): ...
def large_model(use_cudnn_rnn: Any): ...
def test_model(use_cudnn_rnn: Any): ...
def main(_: Any) -> None: ...
