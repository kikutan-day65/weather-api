from django.shortcuts import render
from helper_func import *


# Create your views here.
def index(request):
    return render(request, 'weatherapp/index.html')