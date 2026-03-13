import lightgbm as lgb
from sklearn.model_selection import train_test_split

def train_promo_uplift(df):

    features = [
        "price",
        "promo",
        "dow",
        "month",
        "lag_7",
        "lag_14",
        "rolling_mean_7"
    ]

    df = df.dropna()

    X = df[features]
    y = df["y"]

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2
    )

    model = lgb.LGBMRegressor(
        n_estimators=300,
        learning_rate=0.05
    )

    model.fit(X_train,y_train)

    uplift = model.predict(X_test)

    return model