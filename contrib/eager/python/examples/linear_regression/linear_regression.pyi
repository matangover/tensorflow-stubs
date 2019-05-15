# Stubs for tensorflow.contrib.eager.python.examples.linear_regression.linear_regression (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import tensorflow.contrib.eager as tf
from typing import Any as Any, Optional as Optional

layers: Any

class LinearModel(tf.keras.Model):
    def __init__(self) -> None: ...
    def call(self, xs: Any): ...

def mean_square_loss(model: Any, xs: Any, ys: Any): ...
def fit(model: Any, dataset: Any, optimizer: Any, verbose: bool = ..., logdir: Optional[Any] = ...): ...
def synthetic_dataset(w: Any, b: Any, noise_level: Any, batch_size: Any, num_batches: Any): ...
def synthetic_dataset_helper(w: Any, b: Any, num_features: Any, noise_level: Any, batch_size: Any, num_batches: Any): ...
def main(_: Any) -> None: ...
