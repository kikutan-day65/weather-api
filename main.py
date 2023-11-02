import datetime as dt
import requests
from decouple import config


API_KEY = config("API_KEY")
CITY_NAME = 'Tokyo'

# get latitude and longitude
coordinates_url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
coordinates = requests.get(coordinates_url).json()
LAT, LON = coordinates['coord']['lat'], coordinates['coord']['lon']

# main url
url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

response = requests.get(url).json()
print(response)