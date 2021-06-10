from django.shortcuts import render,redirect
from .models import Pasajero, Viaje
from .filters import ProductFilter

from users.models import CustomUser
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
	viajes = Viaje.objects.all().filter(combi__capacidad__gt=0)
	filter = ProductFilter(request.GET, queryset = viajes)
	if request is not None:
		viajes = filter.qs
		print(filter.qs)
	return render(request, "main/home.html", {"listaViaje":viajes, 'filter' : filter})

def viaje_list(request):
	viajes= Viaje.objects.all().filter(combi__capacidad__gt=0)
	filter = ProductFilter(request.GET, queryset = viajes)
	return render(request, 'main/search.html', {'filter' : filter})

def compra(request,vId,uName):
	viaje = Viaje.objects.filter(id=vId).first()
	user = CustomUser.objects.filter(username=uName).first()
	totalAsientos = viaje.combi.capacidad - viaje.pasajeros.count()
	compra = False
	for i in range(totalAsientos):
		#dni = request.POST.get("pasajero"+)
		dniPasajero = request.POST.get("pasajero"+str(i)) #se que esto esta mal pero despues de que se me borro todo dije fue
		if (dniPasajero is not None):
			pas = Pasajero(usuario = user, estado = "reservado", dni = dniPasajero)
			pas.save()
			viaje.pasajeros.add(pas)
			#viaje.save()
			compra = True
	if compra:
		messages.success(request, 'Compra realizada con exito')
		return redirect("/")
	return render(request, "main/compra.html", {"viaje": viaje, "total":totalAsientos})