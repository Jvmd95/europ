import pandas as pd
import pytest
from europcar.load_dataframe import load_dataframe
import pandas as pd


def test_load_dataframe():
    df = pd.read_csv("tests/test_data.csv")
    assert isinstance(df, pd.DataFrame)
