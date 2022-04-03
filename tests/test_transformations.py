import pytest
from europcar.transformations import birthdate_to_age, hot_encoding, fill_na
import pandas as pd


def test_birthdate_to_age():
    df = pd.read_csv("tests/test_data.csv")
    transform_dict = {"fields": [{"field": "user_birthdate", "new_field": "user_age"}]}
    df = birthdate_to_age(df, transform_dict)

    if "user_age" in df.columns:
        pass
    else:
        raise Exception("No user_age in birthdate_to_age()")


def test_hot_encoding():
    df = pd.read_csv("tests/test_data.csv")
    transform_dict = {"fields": ["vehicle_category"]}
    df = hot_encoding(df, transform_dict)

    if "vehicle_category_large" in df.columns:
        pass
    else:
        raise Exception("")


def test_fill_na():
    df = pd.read_csv("tests/test_data.csv")
    transform_dict = {"fields": [
        {"field": "km", "value": "median"},
        {"field": "user_name", "value": "John Doe"}
      ]}
    df = fill_na(df, transform_dict)

    if df["km"].isnull().values.any():
        raise Exception("")
