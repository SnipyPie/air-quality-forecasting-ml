from app.ingestion.geocoding import get_coordinates
from app.ingestion.pollution_fetcher import get_pollution


def get_current_air_quality(city: str):
    coords = get_coordinates(city)
    pollution = get_pollution(coords["lat"], coords["lon"])

    return {
        "city": city,
        "lat": coords["lat"],
        "lon": coords["lon"],
        "aqi": pollution["aqi"],
        "pm2_5": pollution["pm2_5"],
        "pm10": pollution["pm10"],
        "no2": pollution["no2"],
        "so2": pollution["so2"],
        "o3": pollution["o3"]
    }