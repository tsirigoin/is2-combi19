from django.contrib.auth.forms import PasswordResetForm
from django.http import request, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib.auth import logout as logoutFunct
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .forms import CustomUserCreationForm, UserEditForm
from .models import CustomUser
from main.forms import CustomComentarioForm
from main.models import Viaje, Comentario, Pasajero
import datetime
from django.contrib import messages

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
		viajes_pendientes = Viaje.objects.filter(pasajeros__usuario=response.user, pasajeros__estado='reservado')#.first()
		viajes_finalizados = Viaje.objects.filter(pasajeros__usuario=response.user, pasajeros__estado='finalizado')
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
	
def devolver_pasaje(response, vId):
	user = response.user
	viaje = Viaje.objects.filter(id=vId).first()
	pasajero = Pasajero.objects.filter(usuario=user).first()
	pasajero.delete()
	print(viaje.fecha > (datetime.date.today()+datetime.timedelta(hours=24)))
	if (viaje.fecha >(datetime.date.today()+datetime.timedelta(hours=24))):
		messages.success(response, 'Se le devolvio el 100% del precio del boleto')
	else:
		messages.success(response, 'Se le devolvio el 50% del precio del boleto')
	return redirect('perfil')
	
def password_reset_request(response):
	if response.method == 'POST':
		password_reset_form = PasswordResetForm(response.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_user = CustomUser.objects.get(Q(email=data))
			if associated_user:
				subject = "Reestablecimiento de Contraseña Pedido"
				email_template_name = "password/password_reset_email.txt"
				c = {
					"email": associated_user.email,
					"domain": '127.0.0.1:8000',
					'site_name': 'COMBI-19',
					'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
					'user': associated_user,
					'token': default_token_generator.make_token(associated_user),
					'protocol': 'http',
				}
				email = render_to_string(email_template_name, c)
				try:
					send_mail(subject,email,'admin@combi19.com',[associated_user.email],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Header inválido detectado.')
				return redirect('/accounts/password_reset/done/')
	password_reset_form = PasswordResetForm()
	return render(request=response,template_name='password/password_reset.html',context={'password_reset_form': password_reset_form})
