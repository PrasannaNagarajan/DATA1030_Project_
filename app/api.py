import pandas as pd

DATA_URL = "https://metadata.ffcws.princeton.edu/get_metadata"


def get_metadata():
    return pd.read_csv(DATA_URL, encoding="latin1", low_memory=False)


FOF_dataframe = get_metadata

__all__ = ["get_metadata", "FOF_dataframe"]
