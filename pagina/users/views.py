from django.shortcuts import render, redirect
from django.contrib.auth import logout as logoutFunct
from .forms import CustomUserCreationForm, UserEditForm
from main.forms import CustomComentarioForm
from main.models import Viaje, Comentario

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
		viajes_pendientes = Viaje.objects.filter(pasajeros__usuario__pk=response.user.pk).filter(pasajeros__estado='reservado')
		viajes_finalizados = Viaje.objects.filter(pasajeros__usuario=response.user).filter(pasajeros__estado='finalizado')
	return render(response,'users/perfil.html',{'user': response.user,
		'user_form': user_form, 'viajes_finalizados': viajes_finalizados, 'viajes_pendientes': viajes_pendientes,
	})

def cambiar_membresia(response):
	response.user.toggle_premium()
	response.user.save()
	return redirect('perfil')

def comentarios(response,viaje_id):
	if response.method == 'POST':
		form = CustomComentarioForm(response.POST)
		if form.is_valid():
			via = Viaje.objects.get(pk=viaje_id)
			comentario = Comentario(usuario=response.user,
									texto=form.cleaned_data['texto'],
									viaje=via)
			comentario.save()
			return redirect('comentario', viaje_id)
	else:
		viajes = Viaje.objects.get(pk=viaje_id)
		comentarios = CustomComentarioForm()
		return render(response, 'users/comentarios.html',{'user': response.user, 'viajes': viajes,
	 			'comentarios': comentarios })



def eliminar_comentario(response, comentario_id):
	comentario = Comentario.objects.get(id=comentario_id)
	viaje_id = comentario.viaje.id
	comentario.delete()
	return redirect('comentario', viaje_id)

def modificar_comentario(response,comentario_id):
	if response.method == 'POST':
		form = CustomComentarioForm(response.POST)
		if form.is_valid():
			comentario = Comentario.objects.get(id=comentario_id)
			comentario.texto= form.cleaned_data['texto']
			comentario.save()
			return redirect('editarcomentario', comentario_id)
	else:
		comen = Comentario.objects.get(id=comentario_id)
		comentario = CustomComentarioForm(instance=comen)
		return render(response,'users/comentario.html',{'user': response.user, 'com':comen,
			'comentario': comentario,
	})
