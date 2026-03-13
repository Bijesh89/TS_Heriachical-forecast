from sklearn.metrics import mean_absolute_percentage_error

def evaluate(actual,forecast):

    mape = mean_absolute_percentage_error(
        actual,
        forecast
    )

    return {"MAPE":mape}