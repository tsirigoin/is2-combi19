from django.shortcuts import render
from django.http import HttpResponse
from .models import viaje

# Create your views here.

def home(response):
    listaViaje = viaje.objects.all()
    return render(response, "main/home.html", {"listaViaje":listaViaje})

def register(response):
    return render(response, "main/registro.html", {})