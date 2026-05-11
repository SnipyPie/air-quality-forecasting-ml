from app.ingestion.geocoding import get_coordinates
from app.ingestion.pollution_fetcher import get_pollution

coords = get_coordinates("Delhi")

pollution = get_pollution(coords["lat"], coords["lon"])

print(coords)
print(pollution)