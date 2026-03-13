import pandas as pd

def build_features(df):

    df["dow"] = df["ds"].dt.dayofweek
    df["month"] = df["ds"].dt.month

    df["lag_7"] = df.groupby("unique_id")["y"].shift(7)
    df["lag_14"] = df.groupby("unique_id")["y"].shift(14)

    df["rolling_mean_7"] = (
        df.groupby("unique_id")["y"]
        .rolling(7)
        .mean()
        .reset_index(level=0,drop=True)
    )

    return df