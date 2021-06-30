from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib.auth import logout as logoutFunct
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .forms import CustomUserCreationForm, UserEditForm
from .models import CustomUser
from main.forms import CustomComentarioForm
from main.models import Viaje, Comentario, Pasajero, Test
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
	viajes_pendientes = Viaje.objects.filter(pasajeros__usuario=response.user, pasajeros__estado='reservado')
	viajes_finalizados = Viaje.objects.filter(Q(pasajeros__usuario=response.user) and ~Q(pasajeros__estado='reservado'))
	return render(response,'users/perfil.html',{
		'user': response.user,
		'viajes_finalizados': viajes_finalizados,
		'viajes_pendientes': viajes_pendientes,
	})

def chofer(response):
	viajes_pendientes = Viaje.objects.filter(chofer__user=response.user,estado='reservado')
	historial = Viaje.objects.filter(~Q(estado='reservado')).exclude(~Q(chofer__user=response.user))
	return render(response,'users/chofer.html',{
		'viajes_pendientes': viajes_pendientes,
		'historial': historial,
	})

def editar_perfil(response):
	if response.method == 'POST':
		user_form = UserEditForm(response.POST,instance=response.user)
		if user_form.is_valid():
			user_form.save()
			return redirect('perfil')
	else:
		user_form = UserEditForm(instance=response.user)
	return render(response,'users/editar_perfil.html',{
		'user': response.user,
		'user_form': user_form,
	})

def cambiar_contraseña(response):
	if response.method == 'POST':
		pass_form = PasswordChangeForm(response.user,response.POST)
		if pass_form.is_valid():
			user = pass_form.save()
			update_session_auth_hash(response,user)
			return redirect('perfil')
	else:
		pass_form = PasswordChangeForm(response.user)
	return render(response,'users/cambiar_contraseña.html',{
		'pass_form': pass_form
	})

def cambiar_membresia(response):
	response.user.toggle_premium()
	response.user.save()
	return redirect('perfil')

def ver_viaje(response,vId):
	viaje = Viaje.objects.get(id=vId)
	tests = Test.objects.filter(viaje__id=vId)
	return render(response,'users/ver_viaje.html',{
		'viaje': viaje, 'test': tests
	})

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

def pasaje_perdido(response,vId,pId):
	pasaje = Pasajero.objects.get(id=pId)
	pasaje.estado= 'perdido'
	pasaje.save()
	return redirect('ver_viaje', vId)

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

def cancelar_viaje(response, vId):
	viaje = Viaje.objects.get(id=vId)
	for p in viaje.pasajeros.all():
		associated_user = p.usuario
		if associated_user:
			subject = "Viaje "+str(viaje)+" cancelado"
			email_template_name = "users/viaje_cancelado_email.txt"
			c = {
				"email": associated_user.email,
				"site_name": 'COMBI-19',
				"viaje_nom": str(viaje),
			}
			email = render_to_string(email_template_name,c)
			try:
				send_mail(subject,email,'viajes@combi19.com',[associated_user.email],fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Header inválido detectado.')
		p.cancelar()
		p.save()
	viaje.cancelar()
	viaje.save()
	return redirect('cancelacion_exitosa')

def viaje_en_curso(response, vId):
	viaje = Viaje.objects.get(id=vId)
	for p in viaje.pasajeros.all():
		if p.estado == 'reservado':
			p.en_curso()
			p.save()
	viaje.en_curso()
	viaje.save()
	return redirect('chofer')

def finalizar_viaje(response, vId):
	viaje = Viaje.objects.get(id=vId)
	for p in viaje.pasajeros.all():
		if p.estado == 'viajando':
			p.finalizar()
			p.save()
	viaje.finalizar()
	viaje.save()
	return redirect('chofer')

def cancelacion_exitosa(response):
	return render(response,'users/cancelacion_exitosa.html')

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

def test(response, viaje_id, pasajero_id):
		if response.method == 'POST':
			cant = 0
			form = response.POST
			if 	float(form['test_temperatura'])< 38:
				if form['fiebre']=='fiebreSi':
					cant= cant + 1
				if form['difResp']=='difRespSi':
					cant= cant + 1
				if form['olfato']=='olfatoSi':
					cant= cant + 1
				if form['dolor']=='dolorSi':
					cant= cant + 1
				if cant<2:
					test= Test(
						pasajero = Pasajero.objects.get(pk=pasajero_id),
						viaje = Viaje.objects.get(pk=viaje_id),
						temperatura = form['test_temperatura'],
						estado = 'negativo'
					)
					test.save()
					return redirect('ver_viaje', viaje_id)
				else:
					test= Test(
						pasajero = Pasajero.objects.get(pk=pasajero_id),
						viaje = Viaje.objects.get(pk=viaje_id),
						temperatura = form['test_temperatura'],
						estado = 'positivo'
					)
					test.save()
					return redirect('ver_viaje', viaje_id)
			else:
				test= Test(
					pasajero = Pasajero.objects.get(pk=pasajero_id),
					viaje = Viaje.objects.get(pk=viaje_id),
					temperatura = form['test_temperatura'],
					estado = 'positivo'
				)
				test.save()
				return redirect('ver_viaje', viaje_id)
		else:
			viajes = Viaje.objects.first()
			user = Pasajero.objects.get(pk=pasajero_id)
			return render(response, 'users/test.html',{'usuario': user, 'viaje': viajes })

def editar_test(response,test_id):
	if response.method == 'POST':
		form = response.POST
		test = Test.objects.get(id=test_id)
		test.temperatura= (form['test_temperatura'])
		if form['test_estado'] == 'estadoPosi':
			test.estado = "positivo"
		else:
			test.estado = "negativo"
		test.save()
		return redirect('editar_test', test_id)
	else:
		test = Test.objects.get(id=test_id)
		return render(response,'users/ver_test.html',{'user': response.user, 'test':test,
	})

def eliminar_test(response, test_id):
	test = Test.objects.get(pk=test_id)
	viaje_id = test.viaje.id
	test.delete()
	return redirect('ver_viaje', viaje_id)
