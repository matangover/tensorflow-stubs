# Stubs for tensorflow.contrib.eager.python.examples.spinn.data (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any

POSSIBLE_LABELS: Any
UNK_CODE: int
PAD_CODE: int
SHIFT_CODE: int
REDUCE_CODE: int
WORD_VECTOR_LEN: int
LEFT_PAREN: str
RIGHT_PAREN: str
PARENTHESES: Any

def get_non_parenthesis_words(items: Any): ...
def get_shift_reduce(items: Any): ...
def pad_and_reverse_word_ids(sentences: Any): ...
def pad_transitions(sentences_transitions: Any): ...
def load_vocabulary(data_root: Any): ...
def load_word_vectors(data_root: Any, vocab: Any): ...
def calculate_bins(length2count: Any, min_bin_size: Any): ...
def encode_sentence(sentence: Any, word2index: Any): ...

class SnliData:
    def __init__(self, data_file: Any, word2index: Any, sentence_len_limit: int = ...) -> None: ...
    def num_batches(self, batch_size: Any): ...
    def get_generator(self, batch_size: Any): ...
