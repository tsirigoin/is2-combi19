from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .models import Insumo, Pasajero, Viaje
from .filters import ProductFilter

from users.models import CustomUser, Tarjeta
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers

import datetime
from datetime import date, timedelta

# Create your views here.

def home(request):
	viajes = Viaje.objects.filter(combi__capacidad__gt=0,estado='reservado')
	filter = ProductFilter(request.GET, queryset = viajes)
	if request is not None:
		viajes = filter.qs
	return render(request, "main/home.html", {"listaViaje":viajes, 'filter' : filter})

def viaje_list(request):
	viajes= Viaje.objects.filter(combi__capacidad__gt=0,estado='reservado')
	filter = ProductFilter(request.GET, queryset = viajes)
	return render(request, 'main/search.html', {'filter' : filter})

def ver_insumos(request,vId):
	viaje = Viaje.objects.get(id=vId)
	insumos = viaje.insumo.all()
	pasaje = viaje.pasajeros.filter(usuario=request.user).first()
	return render(request,'main/comprar_insumo.html',{'insumos':insumos,'pasaje':pasaje})

def comprar_insumo(request,pId,iId):
	pasaje = Pasajero.objects.get(id=pId)
	insumo = Insumo.objects.get(id=iId)
	form = request.POST
	cant = int(form['cant'])
	if insumo.cantidadActual > cant:
		if pasaje.insumos:
			aux = eval(pasaje.insumos)
		else:
			aux = dict()
		insumo.cantidadActual = insumo.cantidadActual - cant
		aux[insumo.nombre] = cant
		insumo.save()
		pasaje.insumos = eval(str(aux))
		pasaje.save()
		messages.success(request,'Compra realizada con éxito.')
	else:
		messages.error(request,'Ingresa una cantidad posible.')
	return redirect('perfil')

def compra(request,vId,uName):
	viaje = Viaje.objects.get(id=vId)
	user = CustomUser.objects.get(username=uName)
	totalAsientos = viaje.combi.capacidad - viaje.pasajeros.count()

	compra = False
	for i in range(totalAsientos):
		#dni = request.POST.get("pasajero"+)
		dniPasajero = request.POST.get("pasajero"+str(i)) #se que esto esta mal pero despues de que se me borro todo dije fue
		if (dniPasajero is not None):
			pas = Pasajero(usuario = user, dni = dniPasajero)
			pas.save()
			viaje.pasajeros.add(pas)
			viaje.save()
			compra = True
			if (request.POST.get("guardado")=="si"):
				if (Tarjeta.objects.filter(numero = request.POST.get("numT")).exists()):
					tarjeta = Tarjeta.objects.get(numero=request.POST.get("numT"))
				else:
					tarjeta = Tarjeta(numero = request.POST.get("numT"),fecha= request.POST.get("fechaT"), titular="test")
					tarjeta.save()
				user.tarjetas.add(tarjeta)
				user.save()

	tarjetas = user.test
	if compra:
		messages.success(request, 'Compra realizada con exito')
		return redirect("/")
	return render(request, "main/compra.html", {"viaje": viaje, "total":totalAsientos, "tarjetas":tarjetas})

def checkout(response):
	if response.method == 'POST':
		form = response.POST
		usuario = CustomUser.objects.get(username=response.user.username)
		tarjeta = Tarjeta(	numero=form['tarjeta_codigo'],
								fecha=form['fecha_ven'],
								titular=form['tarjeta_nombre']
							)
		tarjeta.save()
		usuario.tarjetas.add(tarjeta)
		usuario.save()
		return redirect('perfil')
	else:
		return render(response, "main/checkout.html", {'user': response.user })
