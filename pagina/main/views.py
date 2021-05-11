from django.shortcuts import render
from .models import Viaje

# Create your views here.

def home(response):
    listaViaje = Viaje.objects.all()
    return render(response, "main/home.html", {"listaViaje":listaViaje})