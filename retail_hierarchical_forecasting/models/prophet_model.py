from prophet import Prophet
import pandas as pd
from joblib import Parallel, delayed

def train_prophet(group):

    uid, data = group

    model = Prophet()

    model.add_regressor("promo")
    model.add_regressor("price")

    model.fit(data[["ds","y","promo","price"]])

    future = model.make_future_dataframe(periods=30)

    future["promo"] = 0
    future["price"] = data["price"].mean()

    fcst = model.predict(future)

    out = fcst[["ds","yhat"]]

    out["unique_id"] = uid

    return out


def run_prophet_parallel(df):

    groups = list(df.groupby("unique_id"))

    results = Parallel(n_jobs=-1)(
        delayed(train_prophet)(g)
        for g in groups
    )

    forecasts = pd.concat(results)

    forecasts = forecasts.rename(columns={"yhat":"y"})

    return forecasts