import datetime as dt
import requests
from decouple import config


API_KEY = config('API_KEY')


def get_latitude_and_longitude(city, api_key=API_KEY):
    coordinates_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    coordinates = requests.get(coordinates_url).json()
    LAT, LON = coordinates['coord']['lat'], coordinates['coord']['lon']

    return LAT, LON

# # main url
# url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}'

# response = requests.get(url).json()
# print(response)



def main():
    city = 'Tokyo'
    latitude, longitude = get_latitude_and_longitude(city)
    print(latitude)
    print(longitude)


if __name__=='__main__':
    main()