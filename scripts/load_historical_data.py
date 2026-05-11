import pandas as pd
from app.storage.db import SessionLocal
from app.storage.models import PollutionData

df = pd.read_csv("data/raw/delhi_historical.csv")

session = SessionLocal()

for _, row in df.iterrows():
    entry = PollutionData(
        city="Delhi",
        lat=28.61,
        lon=77.20,
        aqi=int(row["aqi"]),
        pm2_5=float(row["pm2_5"]),
        pm10=float(row["pm10"]),
        no2=float(row["no2"]),
        so2=float(row["so2"]),
        o3=float(row["o3"]),
        timestamp=row["timestamp"]
    )
    session.add(entry)

session.commit()
session.close()

print("Historical data loaded")