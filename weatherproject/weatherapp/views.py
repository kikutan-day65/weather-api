from django.shortcuts import render
from .helper_func import *


# Create your views here.
def index(request):
    city = enter_city() # Specify the city from html later
    lat, lon = get_latitude_and_longitude(city)
    current = get_current_weather(lat, lon)
    
    context = {
        'city': city,
        'current': current
    }

    return render(request, 'weatherapp/index.html', context)