import requests

API_KEY = "97c180bc55640868fea80284273c5f6a"

def get_city_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    
    response = requests.get(url)

    # DEBUG PRINT
    print("RAW RESPONSE:", response.text)

    try:
        data = response.json()
    except Exception as e:
        print("JSON Parse Error:", e)
        return None, None

    if not isinstance(data, list) or len(data) == 0:
        print("City not found OR API key error")
        return None, None

    lat = data[0]["lat"]
    lon = data[0]["lon"]
    return lat, lon


if __name__ == "__main__":
    city = input("Enter city name: ")
    lat, lon = get_city_coordinates(city)
    print("Latitude:", lat)
    print("Longitude:", lon)
