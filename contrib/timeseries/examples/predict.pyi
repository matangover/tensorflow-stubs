# Stubs for tensorflow.contrib.timeseries.examples.predict (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any

HAS_MATPLOTLIB: bool
FLAGS: Any

def structural_ensemble_train_and_predict(csv_file_name: Any): ...
def ar_train_and_predict(csv_file_name: Any): ...
def train_and_predict(estimator: Any, csv_file_name: Any, training_steps: Any): ...
def make_plot(name: Any, training_times: Any, observed: Any, all_times: Any, mean: Any, upper_limit: Any, lower_limit: Any) -> None: ...
def main(unused_argv: Any) -> None: ...
