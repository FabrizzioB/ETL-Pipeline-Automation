import requests
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

from config import *

#ExtractTransformLoad
def get_weather(city: str):

    city_info = None

    for item in cities_portugal:
        if item["city"].lower() == city.lower():
            city_info = item
            break

    # Extract latitude and longitude
    lat = city_info['lat']
    lon = city_info['lon']

    complete_url = f"{WEATHER_API_BASE_URL}?lat={lat}&lon={lon}&lang={DEFAULT_LANGUAGE}&units={UNITS}&appid={API_KEY}"
    response = requests.get(complete_url)
    return response.json()


def print_weather_info(weather_data):
    print(f"Weather Information for {weather_data['name']}, {weather_data['sys']['country']}:")
    print("=" * 50)

    coord = weather_data['coord']
    print(f"Coordinates: Lat {coord['lat']}, Lon {coord['lon']}")

    weather = weather_data['weather'][0]
    print(f"Weather: {weather['main']} - {weather['description']}")

    main = weather_data['main']
    print(f"Temperature: {main['temp']}°C (Feels like {main['feels_like']}°C)")
    print(f"Min Temperature: {main['temp_min']}°C, Max Temperature: {main['temp_max']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Pressure: {main['pressure']} hPa")

    wind = weather_data['wind']
    print(f"Wind Speed: {wind['speed']} m/s at {wind['deg']}°")

    clouds = weather_data['clouds']['all']
    print(f"Cloudiness: {clouds}%")

    sys = weather_data['sys']
    print(f"Sunrise: {convert_unix_to_time(sys['sunrise'])}\nSunset: {convert_unix_to_time(sys['sunset'])}")

    print("=" * 50)


def convert_unix_to_time(unix_timestamp):
    from datetime import datetime
    return datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

if __name__=="__main__":
    city_mapping = {
        "1": "Lisbon",
        "2": "Porto",
        "3": "Braga",
        "4": "Coimbra",
        "5": "Faro",
        "6": "Evora",
        "7": "Leiria",
        "8": "Aveiro",
        "9": "Setubal",
        "10": "Viseu",
        "11": "Guarda",
        "12": "Distrito De Santarem",
        "13": "Castelo Branco",
        "14": "Viana Do Castelo",
        "15": "Vila Real",
        "16": "Beja",
        "17": "Braganca",
        "18": "Portalegre",
        "19": "Funchal",
        "20": "Ponta Delgada"
    }

    number = input("Select the city:\n"
                    "1-Lisbon\n"
                    "2-Porto\n"
                    "3-Braga\n"
                    "4-Coimbra\n"
                    "5-Faro\n"
                    "6-Évora\n"
                    "7-Leiria\n"
                    "8-Aveiro\n"
                    "9-Setúbal\n"
                    "10-Viseu\n"
                    "11-Guarda\n"
                    "12-Santarém\n"
                    "13-Castelo Branco\n"
                    "14-Viana do Castelo\n"
                    "15-Vila Real\n"
                    "16-Beja\n"
                    "17-Bragança\n"
                    "18-Portalegre\n"
                    "19-Funchal\n"
                    "20-Ponta Delgada\n")

    information = get_weather(city_mapping[number])
    print_weather_info(information)