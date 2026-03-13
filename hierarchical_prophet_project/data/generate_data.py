import pandas as pd
import numpy as np

def generate_data():

    np.random.seed(42)

    dates = pd.date_range("2020-01-01", periods=200)

    regions = ["Region_A", "Region_B"]
    products = ["Product_1", "Product_2"]

    records = []

    for r in regions:
        for p in products:
            base = np.random.randint(40,100)

            values = base + np.sin(np.arange(200)/10)*10 + np.random.normal(0,3,200)

            for d,v in zip(dates,values):
                records.append({
                    "ds": d,
                    "region": r,
                    "product": p,
                    "y": v
                })

    df = pd.DataFrame(records)

    df["unique_id"] = df["region"] + "_" + df["product"]

    return df