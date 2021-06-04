from django.shortcuts import render
from .models import Viaje
from .filters import ProductFilter

# Create your views here.

def home(response):
    viajes = Viaje.objects.all().filter(combi__capacidad__gt=0)
    return render(response, "main/home.html", {"listaViaje":viajes})

def viaje_list(request):
	viajes= Viaje.objects.all().filter(combi__capacidad__gt=0)
	filter = ProductFilter(request.GET, queryset = viajes)
	return render(request, 'main/search.html', {'filter' : filter})