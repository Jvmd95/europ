import pandas as pd


def load_dataframe(source):
    path = f"{source['path']}{source['dataset']}.{source['format']}"
    if source['format'] == 'csv':
        df = pd.read_csv(path)
    elif source['format'] == 'jsonl':
        df = pd.read_json(path)
    elif source['format'] == 'parquet':
        df = pd.read_parquet(path)
    else:
        raise Exception("Wrong format: input file must be csv, jsonl or parquet format")

    return df
