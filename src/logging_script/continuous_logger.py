import sys
import os

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)


import time
import csv
from datetime import datetime
from src.api.get_coordinates import get_city_coordinates
from src.api.fetch_pollution import get_pollution_data


CITY = "Delhi"                       # You can change it anytime
INTERVAL_MINUTES = 15                # every 15 minutes
CSV_PATH = "data/raw/pollution_log.csv"

def write_header_if_needed():
    try:
        with open(CSV_PATH, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp", "city", "lat", "lon",
                "aqi", "pm2_5", "pm10", "no2", "so2", "o3"
            ])
    except FileExistsError:
        pass  # CSV already exists

def log_pollution_data():
    lat, lon = get_city_coordinates(CITY)
    if lat is None or lon is None:
        print("City not found. Cannot log data.")
        return

    pollution = get_pollution_data(lat, lon)
    if pollution is None:
        print("Error fetching pollution data.")
        return

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        CITY,
        lat, lon,
        pollution["aqi"],
        pollution["pm2_5"],
        pollution["pm10"],
        pollution["no2"],
        pollution["so2"],
        pollution["o3"],
    ]

    with open(CSV_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

    print("Logged:", row)


if __name__ == "__main__":
    write_header_if_needed()

    while True:
        log_pollution_data()
        print(f"Next log in {INTERVAL_MINUTES} minutes...")
        time.sleep(INTERVAL_MINUTES * 60)
