from data.generate_data import generate_data
from models.prophet_model import train_prophet
from utils.hierarchy import build_hierarchy
from reconciliation.reconcile import reconcile_forecasts
import pandas as pd


def main():

    print("Generating synthetic data...")
    df = generate_data()

    print("Training Prophet models...")
    forecasts = train_prophet(df)

    forecasts["unique_id"] = forecasts["unique_id"].astype(str).str.strip()

    print("Building hierarchy...")
    S, tags = build_hierarchy()

    bottom_ids = list(S.columns)

    # keep only bottom forecasts
    forecasts = forecasts[forecasts["unique_id"].isin(bottom_ids)]

    # Add missing hierarchy levels
    future_dates = forecasts["ds"].unique()
    agg_levels = ["Total","Region_A","Region_B"]

    extra_rows = []

    for level in agg_levels:
        for d in future_dates:
            extra_rows.append({
                "unique_id": level,
                "ds": d,
                "y": 0
            })

    extra_df = pd.DataFrame(extra_rows)

    forecasts = pd.concat([forecasts, extra_df], ignore_index=True)

    print("\nReconciling forecasts...")

    final_forecasts = reconcile_forecasts(
        forecasts,
        S,
        tags
    )

    print("\nReconciled forecast sample:")
    print(final_forecasts.head())


if __name__ == "__main__":
    main()                          