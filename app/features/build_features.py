import pandas as pd
from app.storage.db import engine

def load_data():
    query = "SELECT * FROM pollution_data ORDER BY timestamp"
    df = pd.read_sql(query, engine)
    return df

def build_features(df):
    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    df["pm2_5_roll"] = df["pm2_5"].rolling(window=3).mean()
    df["pm10_roll"] = df["pm10"].rolling(window=3).mean()

    df["aqi_future_1h"] = df["aqi"].shift(-4)

    df = df.dropna()

    return df