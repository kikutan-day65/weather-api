from django.shortcuts import render
from .helper_func import *
import datetime


# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city'].title()
    else:
        city = 'Tokyo'
        
    lat, lon = get_latitude_and_longitude(city)
    current = get_current_weather(lat, lon)
    temperature = convert_to_celsius(current['main']['temp'])
    icon = current['weather'][0]['icon']
    description = current['weather'][0]['description']
    day = datetime.date.today()
    
    
    context = {
        'city': city,
        'temp': temperature,
        'icon': icon,
        'description': description,
        'day': day,
    }

    return render(request, 'weatherapp/index.html', context)