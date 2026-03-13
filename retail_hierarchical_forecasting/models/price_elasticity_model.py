import numpy as np
import statsmodels.api as sm

def estimate_elasticity(df):

    df = df[df["price"]>0]

    df["log_demand"] = np.log(df["y"]+1)
    df["log_price"] = np.log(df["price"])

    X = sm.add_constant(df["log_price"])

    model = sm.OLS(df["log_demand"],X).fit()

    elasticity = model.params["log_price"]

    return elasticity