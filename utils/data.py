import numpy as np
import pandas as pd


def get_data(size: int) -> pd.DataFrame:
    """
    size: int, the number of rows for the generated dataframe.

    Return: pandas.DataFrame, a simple dataframe with random values.
    """
    y = np.random.standard_normal(size)
    categories = np.random.choice(5, size)
    index = pd.date_range("2023-01-01 00:00:00", pd.to_datetime(
        "2023-01-01 00:00:00") + pd.Timedelta(days=size-1), freq="D")
    df = pd.DataFrame({"value": y, "category": categories}, index=index)
    df.index.name = "Datetime"
    return df
