import pandas as pd
import numpy as np

def generate_data():

    np.random.seed(42)

    dates = pd.date_range("2020-01-01", periods=365)

    regions = ["North","South"]
    stores = ["Store_1","Store_2"]
    categories = ["Beverages","Snacks"]
    skus = ["SKU_A","SKU_B"]

    rows = []

    for r in regions:
        for s in stores:
            for c in categories:
                for sku in skus:

                    base = np.random.randint(20,80)

                    for d in dates:

                        promo = np.random.binomial(1,0.15)

                        price = np.random.uniform(8,12)

                        demand = (
                            base
                            + 10*promo
                            -1.5*price
                            + np.sin(d.dayofyear/365*2*np.pi)*5
                            + np.random.normal(0,2)
                        )

                        rows.append({
                            "ds":d,
                            "region":r,
                            "store":s,
                            "category":c,
                            "sku":sku,
                            "price":price,
                            "promo":promo,
                            "y":max(demand,0)
                        })

    df = pd.DataFrame(rows)

    df["unique_id"] = (
        df["region"]
        +"_"+df["store"]
        +"_"+df["category"]
        +"_"+df["sku"]
    )

    return df