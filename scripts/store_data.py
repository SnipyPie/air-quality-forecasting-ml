from app.storage.db import SessionLocal
from app.storage.models import PollutionData
from app.ingestion.geocoding import get_coordinates
from app.ingestion.pollution_fetcher import get_pollution

session = SessionLocal()

coords = get_coordinates("Delhi")
pollution = get_pollution(coords["lat"], coords["lon"])

entry = PollutionData(
    city=coords["city"],
    lat=coords["lat"],
    lon=coords["lon"],
    aqi=pollution["aqi"],
    pm2_5=pollution["pm2_5"],
    pm10=pollution["pm10"],
    no2=pollution["no2"],
    so2=pollution["so2"],
    o3=pollution["o3"]
)

session.add(entry)
session.commit()
session.close()

print("Data stored successfully")