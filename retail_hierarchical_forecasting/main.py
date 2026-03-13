from pipeline.forecasting_pipeline import run_pipeline

def main():

    forecasts, promo_model, elasticity = run_pipeline()

    print("Forecast sample")
    print(forecasts.head())

    print("\nEstimated price elasticity:",elasticity)


if __name__ == "__main__":
    main()