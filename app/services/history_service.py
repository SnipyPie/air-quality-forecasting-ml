import pandas as pd
from app.storage.db import engine


def get_history_data(city: str, date: str):
    query = """
    SELECT *
    FROM pollution_data
    WHERE city = %s
    AND DATE(timestamp) = %s
    ORDER BY timestamp ASC
    """

    df = pd.read_sql(query, engine, params=(city, date))

    if df.empty:
        return {"message": "No data found for given date"}

    result = []

    for _, row in df.iterrows():
        result.append({
            "timestamp": row["timestamp"],
            "aqi": row["aqi"],
            "pm2_5": row["pm2_5"],
            "pm10": row["pm10"],
            "no2": row["no2"],
            "so2": row["so2"],
            "o3": row["o3"]
        })

    return result