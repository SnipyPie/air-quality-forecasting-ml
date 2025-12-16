import requests
import csv
import os
import time
from datetime import datetime, timedelta
import sys

# --- Fix path so imports & CSV work everywhere ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
sys.path.append(PROJECT_ROOT)

from src.api.get_coordinates import get_city_coordinates

API_KEY = "778ebb4aa31e8366798f35550856eb3b"

CITY = "Delhi"
DAYS = 90  # last 90 days (ideal for ML)

# CSV path (absolute & safe)
CSV_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
CSV_PATH = os.path.join(CSV_DIR, "pollution_history.csv")


def fetch_historical_pollution(lat, lon, start_ts, end_ts):
    url = (
        "http://api.openweathermap.org/data/2.5/air_pollution/history"
        f"?lat={lat}&lon={lon}&start={start_ts}&end={end_ts}&appid={API_KEY}"
    )
    response = requests.get(url)
    return response.json()


def write_header_if_needed():
    os.makedirs(CSV_DIR, exist_ok=True)  # <-- CREATE FOLDER IF NOT EXISTS

    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "city",
                "lat",
                "lon",
                "aqi",
                "pm2_5",
                "pm10",
                "no2",
                "so2",
                "o3"
            ])


def main():
    lat, lon = get_city_coordinates(CITY)
    if lat is None:
        print("City not found")
        return

    write_header_if_needed()

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=DAYS)

    print(f"Fetching {DAYS} days of historical data for {CITY}...")

    current = start_time

    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)

        while current < end_time:
            next_hour = current + timedelta(hours=1)

            start_ts = int(current.timestamp())
            end_ts = int(next_hour.timestamp())

            data = fetch_historical_pollution(lat, lon, start_ts, end_ts)

            if "list" in data and len(data["list"]) > 0:
                item = data["list"][0]

                row = [
                    datetime.utcfromtimestamp(item["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
                    CITY,
                    lat,
                    lon,
                    item["main"]["aqi"],
                    item["components"]["pm2_5"],
                    item["components"]["pm10"],
                    item["components"]["no2"],
                    item["components"]["so2"],
                    item["components"]["o3"],
                ]

                writer.writerow(row)
                print("Saved:", row[0])

            current = next_hour
            time.sleep(1)  # rate-limit safe

    print("Historical data extraction completed.")


if __name__ == "__main__":
    main()
