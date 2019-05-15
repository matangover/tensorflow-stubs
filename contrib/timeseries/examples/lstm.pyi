# Stubs for tensorflow.contrib.timeseries.examples.lstm (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.contrib.timeseries.python.timeseries import model as ts_model, state_management as state_management
from typing import Any as Any, Optional as Optional

HAS_MATPLOTLIB: bool

class _LSTMModel(ts_model.SequentialTimeSeriesModel):
    def __init__(self, num_units: Any, num_features: Any, exogenous_feature_columns: Optional[Any] = ..., dtype: Any = ...) -> None: ...
    def initialize_graph(self, input_statistics: Optional[Any] = ...) -> None: ...
    def get_start_state(self): ...

def train_and_predict(csv_file_name: Any = ..., training_steps: int = ..., estimator_config: Optional[Any] = ..., export_directory: Optional[Any] = ...): ...
def main(unused_argv: Any) -> None: ...
