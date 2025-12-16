import requests

API_KEY = "97c180bc55640868fea80284273c5f6a"

def get_pollution_data(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)
    print("RAW POLLUTION RESPONSE:", response.text)

    data = response.json()

    if "list" not in data:
        print("Error fetching pollution data")
        return None

    info = data["list"][0]

    result = {
        "aqi": info["main"]["aqi"],
        "pm2_5": info["components"]["pm2_5"],
        "pm10": info["components"]["pm10"],
        "no2": info["components"]["no2"],
        "so2": info["components"]["so2"],
        "o3": info["components"]["o3"],
    }

    return result


# Test Run
if __name__ == "__main__":
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")

    data = get_pollution_data(lat, lon)
    print("Pollution Data:", data)
