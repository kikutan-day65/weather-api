import datetime as dt
import requests
from decouple import config


API_KEY = config("API_KEY")

CITY_NAME = 'Tokyo'

# get latitude and longitude
coordinates_url = f"http://api.openweathermap.org/geo/1.0/direct?q={CITY_NAME}&appid={API_KEY}"
coordinates = requests.get(coordinates_url).json()
LAT, LON = coordinates[0]['lat'], coordinates[0]['lon']

# main url
url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

response = requests.get(url).json()
print(response)