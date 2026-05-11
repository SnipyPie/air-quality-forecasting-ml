import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import joblib

from app.features.build_features import load_data, build_features

df = load_data()
df = build_features(df)

features = [
    "pm2_5",
    "pm10",
    "no2",
    "so2",
    "o3",
    "pm2_5_roll",
    "pm10_roll",
    "hour",
    "day_of_week"
]

target = "aqi_future_1h"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(n_estimators=100),
    "GradientBoosting": GradientBoostingRegressor()
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds) ** 0.5
    r2 = r2_score(y_test, preds)

    results[name] = {"MAE": mae, "RMSE": rmse, "R2": r2}

    print(f"\n{name}")
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2:", r2)

best_model_name = min(results, key=lambda x: results[x]["RMSE"])
best_model = models[best_model_name]

joblib.dump(best_model, "artifacts/models/best_model.pkl")

print(f"\nBest Model: {best_model_name}")