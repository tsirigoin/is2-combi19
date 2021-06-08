from django.shortcuts import render
from .models import Viaje
from .filters import ProductFilter

# Create your views here.

def home(request):
	viajes = Viaje.objects.all().filter(combi__capacidad__gt=0)
	filter = ProductFilter(request.GET, queryset = viajes)
	if request is not None:
		viajes = filter.qs
	return render(request, "main/home.html", {"listaViaje":viajes, 'filter' : filter})

def viaje_list(request):
	viajes= Viaje.objects.all().filter(combi__capacidad__gt=0)
	filter = ProductFilter(request.GET, queryset = viajes)
	return render(request, 'main/search.html', {'filter' : filter})

def compra(request,vId):
	viaje = Viaje.objects.filter(id=vId).first()
	return render(request, "main/compra.html", {"viaje": viaje})