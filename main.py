import datetime as dt
import requests
from decouple import config


API_KEY = config('API_KEY')


def get_latitude_and_longitude(city, api_key=API_KEY):
    coordinates_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    coordinates = requests.get(coordinates_url).json()
    LAT, LON = coordinates['coord']['lat'], coordinates['coord']['lon']

    return LAT, LON


def get_current_weather(latitude, longitude, api=API_KEY):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}'
    response = requests.get(url).json()
    
    return response


def covert_to_celsius(kelvin):
    celsius = kelvin - 273.15

    return celsius


def main():
    city = 'Tokyo'
    latitude, longitude = get_latitude_and_longitude(city)
    get_current_weather(latitude, longitude)


if __name__=='__main__':
    main()