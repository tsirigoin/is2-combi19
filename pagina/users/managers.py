from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
	"""
	Manejador de modelo en el que el usuario tiene nombre de usuario y correo electrónico únicos. 
	"""
	
	def create_user(self,email,password,**extra_fields):
		"""
		Crear y guardar un usuario con el correo electrónico, contraseña y nombre de usuario proporcionados
		"""
		if not email:
			raise ValueError(_('Se debe proporcionar un correo electrónico'))
		email = self.normalize_email(email)
		user = self.model(email=email,**extra_fields)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self,email,password,**extra_fields):
		"""
		Crear y guardar un sysop con el correo electrónico, contraseña y nombre de usuario proporcionados
		"""
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)
		extra_fields.setdefault('is_active',True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Un superusuario debe tener permisos de staff'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Un superusuario debe tener permisos de sysop'))
		return self.create_user(email,password,**extra_fields)
	