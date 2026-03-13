from data.generate_synthetic_data import generate_data
from features.feature_engineering import build_features
from models.prophet_model import run_prophet_parallel
from models.promotion_uplift_model import train_promo_uplift
from models.price_elasticity_model import estimate_elasticity

def run_pipeline():

    df = generate_data()

    df = build_features(df)

    promo_model = train_promo_uplift(df)

    elasticity = estimate_elasticity(df)

    forecasts = run_prophet_parallel(df)

    return forecasts, promo_model, elasticity