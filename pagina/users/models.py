from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

from .managers import CustomUserManager

class CustomUser(AbstractUser):
	username = models.CharField(_('Nombre de usuario'),max_length=40,primary_key=True,unique=True)
	email = models.EmailField(_('Dirección de correo electrónico'),unique=True)
	first_name = models.CharField(_('Nombre'),max_length=150)
	last_name = models.CharField(_('Apellido'),max_length=150)
	last_login = models.DateTimeField(_('Última conexión'),auto_now=True)
	fecha_nacimiento = models.DateField(_('Fecha de nacimiento'))

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = [
		'email',
		'first_name',
		'last_name',
		'fecha_nacimiento',
	]

	objects = CustomUserManager()

	def __str__(self):
		return self.username

class Chofer(models.Model):
	user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True)
	dni = models.CharField(max_length=12,unique=True)
	contacto = models.CharField(max_length=20)
	def __str__(self):
		return str(self.user)