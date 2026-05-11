import requests
from app.core.config import OPENWEATHER_API_KEY

BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_coordinates(city):
    params = {
        "q": city,
        "limit": 1,
        "appid": OPENWEATHER_API_KEY
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        raise Exception(f"API failed with status {response.status_code}")

    data = response.json()

    if not data:
        raise Exception("City not found")

    return {
        "city": city,
        "lat": data[0]["lat"],
        "lon": data[0]["lon"]
    }