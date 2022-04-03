import pytest
from europcar.sink_dataframe import sink_dataframe
import pandas as pd


def test_load_json():
    df = pd.read_csv("tests/test_data.csv")

    sink = {
        "path": "./",
        "dataset": "test_data_sink",
        "format": "csv"
    }

    sink_dataframe(df, sink)

    df1 = pd.read_csv("./test_data_sink.csv")

    assert df.equals(df1) == True
