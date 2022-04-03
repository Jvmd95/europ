import pandas as pd


def sink_dataframe(df, sink):
    path = f"{sink['path']}{sink['dataset']}.{sink['format']}"
    if sink['format'] == 'csv':
        df.to_csv(path, index=False)
    elif sink['format'] == 'jsonl':
        df.to_json(path_or_buf=path, orient='records', lines=True)
    elif sink['format'] == 'parquet':
        df.to_parquet(path, index=False)
    else:
        raise Exception("Wrong format: sink file must be csv, jsonl or parquet format")
