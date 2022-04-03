import pandas as pd


def birthdate_to_age(df, transform_dict):
    for field_dict in transform_dict["fields"]:
        birthdate_col = field_dict["field"]
        new_col = field_dict["new_field"]
        df[birthdate_col] = pd.to_datetime(df[birthdate_col])
        df[new_col] = df[birthdate_col].apply(lambda x: (pd.datetime.now().year - x.year))

    return df


def hot_encoding(df, transform_dict):
    df = pd.get_dummies(data=df, columns=transform_dict["fields"])

    return df


def fill_na(df, transform_dict):
    for field_dict in transform_dict["fields"]:
        na_col = field_dict["field"]
        parameter = field_dict["value"]

        if parameter == "mean":
            df[na_col].fillna((df[na_col].mean()), inplace=True)
        elif parameter == "mode":
            df[na_col].fillna((df[na_col].mode()[0]), inplace=True)
        elif parameter == "median":
            df[na_col].fillna((df[na_col].median()), inplace=True)
        else:
            df[na_col].fillna(parameter, inplace=True)

    return df


def transformation_orchestrator(df, transformation_list):
    for transform_dict in transformation_list:
        if transform_dict["transform"] == "birthdate_to_age":
            df = birthdate_to_age(df, transform_dict)
        if transform_dict["transform"] == "hot_encoding":
            df = hot_encoding(df, transform_dict)
        if transform_dict["transform"] == "fill_empty_values":
            df = fill_na(df, transform_dict)

    return df

