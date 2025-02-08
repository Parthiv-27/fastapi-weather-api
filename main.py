import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

# API Configuration
API_KEY = "cf71f639712dbeb4d3330a69deea1c2f"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
def get_weather(city: str):
    """
    Fetches real-time weather data for a given city from OpenWeatherMap API.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    # Handle non-200 responses from OpenWeatherMap API
    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="Invalid API Key. Please check your OpenWeatherMap API key.")

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="City not found. Please check the city name and try again.")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data.")

    # Extract necesary information
    data = response.json()

    weather_info = {
        "city": data.get("name", "Unknown"),
        "country": data["sys"].get("country", "Unknown"),
        "temperature": data["main"].get("temp", "N/A"),
        "feels_like": data["main"].get("feels_like", "N/A"),
        "humidity": data["main"].get("humidity", "N/A"),
        "weather": data["weather"][0].get("description", "N/A"),
        "wind_speed": data["wind"].get("speed", "N/A")
    }

    return weather_info
