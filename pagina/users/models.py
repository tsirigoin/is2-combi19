from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator,ValidationError,MinValueValidator
from datetime import date
import datetime

from .managers import CustomUserManager

class Tarjeta(models.Model):
    numero = models.IntegerField(max_length=19,validators=[MinLengthValidator(16)],unique=True)
    fecha = models.DateField()
    titular = models.CharField(max_length=40)

    def __str__(self):
        return "Tarjeta terminada en "+str(self.numero[-4:])

class CustomUser(AbstractUser):
	username = models.CharField(_('Nombre de usuario'),max_length=40,primary_key=True,unique=True)
	email = models.EmailField(_('Dirección de correo electrónico'),unique=True)
	first_name = models.CharField(_('Nombre'),max_length=150)
	last_name = models.CharField(_('Apellido'),max_length=150)
	last_login = models.DateTimeField(_('Última conexión'),auto_now=True)
	fecha_nacimiento = models.DateField(_('Fecha de nacimiento'))
	has_premium = models.BooleanField(_('Posee membresía premium'),default=False)
	tarjetas = models.ManyToManyField(Tarjeta,blank=True)
	fecha_vencimiento = models.DateField(_('Fecha de vencimiento'))

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = [
		'email',
		'first_name',
		'last_name',
		'fecha_nacimiento',
	]

	objects = CustomUserManager()

	def clean(self):
		if CustomUser.objects.filter(email=self.email).exclude(pk=self.pk).exists():
			raise ValidationError({'email': _('El correo electrónico ingresado ya se encuentra en uso.')})
		today = date.today()
		edad = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
		if edad <= 18:
			raise ValidationError({'fecha_nacimiento': _('Debe ser mayor que 18')})
	def __str__(self):
		return self.username
	def toggle_premium(self):
		if self.has_premium:
			self.has_premium = False
		else:
			self.has_premium = True

	def is_premium (self):
		if self.has_premium:
			return True
		else:
			return False

class Chofer(models.Model):
	user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True)
	dni = models.CharField(max_length=12,unique=True,validators=[MinLengthValidator(6)])
	contacto = models.CharField(max_length=20)
	def __str__(self):
		return (str(self.user.first_name)+" "+str(self.user.last_name))
