from prophet import Prophet
import pandas as pd

def train_prophet(df):

    forecasts = []

    for uid, group in df.groupby("unique_id"):

        model = Prophet()

        model.fit(group[["ds","y"]])

        future = model.make_future_dataframe(periods=30)

        fcst = model.predict(future)[["ds","yhat"]]

        fcst["unique_id"] = uid

        forecasts.append(fcst)

    forecasts = pd.concat(forecasts)

    forecasts = forecasts.rename(columns={"yhat":"y"})

    return forecasts