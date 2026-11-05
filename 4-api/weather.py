import requests

def geocode(place:str) -> (float, float):
    url = "https://portal.app.cent-su.org/api/weather/geocode"
    params = {
        "language": "en",
        "count": 2,
        "place": place,
    }
    headers = {
        "accept": "application/json",
        "X-API-KEY": "6f8517d137a6ef5b59e0e7ac",
    }

    response = requests.get(url, params=params, 
                            headers=headers, timeout=30)
    results = response.json().get("results")
    response.raise_for_status()
    if not results:
        return None, None
    return results[0]['latitude'], results[0]['longitude']

def weather(lat, lon):
    url = "https://portal.app.cent-su.org/api/weather/geocode"
    params={"units": "imperial", "lon": lon, "lat": lat},
    headers={
            "accept": "application/json",
            "X-API-KEY": CENT_API_KEY,
        }
    response = requests.get(url, params=params, 
                                headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()["current"]["temperature_2m"]

if __name__ == "__main__":
    import dotenv
    import os

    dotenv.load_dotenv(".env")
    CENT_API_KEY = os.getenv("CENT_API_KEY")

    #smoke test
    lat, lon = geocode("Syracuse, NY")
    temp = weather(lat, lon)
    print(f"Temperature of Syracuse, NY: {temp}F (lat: {lat}, lon: {lon})")