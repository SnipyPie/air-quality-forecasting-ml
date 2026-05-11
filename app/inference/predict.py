import joblib
import pandas as pd
from app.ingestion.geocoding import get_coordinates
from app.ingestion.pollution_fetcher import get_pollution
from app.storage.db import engine

model = joblib.load("artifacts/models/best_model.pkl")

def get_latest_features(city):
    coords = get_coordinates(city)
    pollution = get_pollution(coords["lat"], coords["lon"])

    query = "SELECT * FROM pollution_data ORDER BY timestamp DESC LIMIT 3"
    df = pd.read_sql(query, engine)

    df = df.sort_values("timestamp")

    new_row = {
        "pm2_5": pollution["pm2_5"],
        "pm10": pollution["pm10"],
        "no2": pollution["no2"],
        "so2": pollution["so2"],
        "o3": pollution["o3"]
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    df["pm2_5_roll"] = df["pm2_5"].rolling(3).mean()
    df["pm10_roll"] = df["pm10"].rolling(3).mean()

    df = df.dropna()

    latest = df.iloc[-1]

    features = [
        latest["pm2_5"],
        latest["pm10"],
        latest["no2"],
        latest["so2"],
        latest["o3"],
        latest["pm2_5_roll"],
        latest["pm10_roll"],
        latest["hour"],
        latest["day_of_week"]
    ]

    return features

def predict_aqi(city):
    features = get_latest_features(city)
    prediction = model.predict([features])[0]
    return prediction