import streamlit as st
import requests
import pandas as pd

st.title("Challenge 4-1-3 ~ Weather App")

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
    response.raise_for_status()
    data = response.json()
    if len(data['results']) == 0:
        raise ValueError(f"No results found for {place}")

    lat = data['results'][0]['latitude']
    lon = data['results'][0]['longitude']
    return lat, lon

def current_weather(lat, lon):
    """Return the current temperature in Fahrenheit for the given coordinates."""
    response = requests.get(
        "https://portal.app.cent-su.org/api/weather/current",
        params={"units": "imperial", "lon": lon, "lat": lat},
        headers={
            "accept": "application/json",
            "X-API-KEY": os.environ["WEATHER_API_KEY"],
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["current"]["temperature_2m"]

location = st.text_input("Enter a location (city, state):", "Syracuse, New York")
if location:
    try:
        lat, lon = geocode(location)
        st.write(f"Coordinates for {location}: Latitude: {lat}, Longitude: {lon}")
    except Exception as e:
        st.error(f"Error: {e}")

