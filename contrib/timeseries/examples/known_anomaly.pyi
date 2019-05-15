# Stubs for tensorflow.contrib.timeseries.examples.known_anomaly (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any as Any

HAS_MATPLOTLIB: bool

def state_space_estimator(exogenous_feature_columns: Any): ...
def autoregressive_estimator(exogenous_feature_columns: Any): ...
def train_and_evaluate_exogenous(estimator_fn: Any, csv_file_name: Any = ..., train_steps: int = ...): ...
def make_plot(name: Any, training_times: Any, observed: Any, all_times: Any, mean: Any, upper_limit: Any, lower_limit: Any, anomaly_locations: Any) -> None: ...
def main(unused_argv: Any) -> None: ...
