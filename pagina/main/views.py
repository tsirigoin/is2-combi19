from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import viaje, usuario

# Create your views here.

def home(response):
    listaViaje = viaje.objects.all()
    return render(response, "main/home.html", {"listaViaje":listaViaje})