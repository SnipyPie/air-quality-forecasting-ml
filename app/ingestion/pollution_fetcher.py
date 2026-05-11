import requests
from app.core.config import OPENWEATHER_API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution"

def get_pollution(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Pollution API failed: {response.status_code}")

    data = response.json()

    main = data["list"][0]["main"]
    comp = data["list"][0]["components"]

    return {
        "aqi": main["aqi"],
        "pm2_5": comp["pm2_5"],
        "pm10": comp["pm10"],
        "no2": comp["no2"],
        "so2": comp["so2"],
        "o3": comp["o3"]
    }