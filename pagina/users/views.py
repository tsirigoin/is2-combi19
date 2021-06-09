from django.shortcuts import render, redirect
from django.contrib.auth import logout as logoutFunct
from .forms import CustomUserCreationForm, UserEditForm,CustomComentarioForm
from main.models import Viaje

# Create your views here.
def register(response):
	if response.method == 'POST':
		form = CustomUserCreationForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = CustomUserCreationForm()
	return render(response,'users/registro.html',{'form': form})

def logout(response):
	logoutFunct(response)
	return render(response,'registration/logout.html')

def perfil(response):
	if response.method == 'POST':
		user_form = UserEditForm(response.POST,instance=response.user)
		if user_form.is_valid():
			user_form.save()
			return redirect('perfil')
	else:
		user_form = UserEditForm(instance=response.user)
		viajes_pendientes = Viaje.objects.filter(pasajeros__usuario=response.user).filter(pasajeros__estado='reservado')
		viajes_finalizados = Viaje.objects.filter(pasajeros__usuario=response.user).filter(pasajeros__estado='finalizado')
	return render(response,'users/perfil.html',{'user': response.user,
		'user_form': user_form, 'viajes_finalizados': viajes_finalizados, 'viajes_pendientes': viajes_pendientes,
	})

	def comentarios(response):
		viajes_finalizados = Viaje.objects.first()
		comentarios = CustomComentarioForm()
		return render(response, 'user/comentarios.html',{'viajes_finalizados': viajes_finalizados, 'comentarios': comentarios})
