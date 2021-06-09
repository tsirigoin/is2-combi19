from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from main.models import Comentario

class CustomDateInput(forms.DateInput):
	input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repita su contraseña',widget=forms.PasswordInput)
	accept = forms.BooleanField(label="Acepto los Términos y Condiciones")

	class Meta(UserCreationForm):
		model = CustomUser
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			'fecha_nacimiento',
			'accept',
		)
		widgets = {
			'fecha_nacimiento': CustomDateInput()
		}
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return password2


	def save(self,commit=True):
		user = super(UserCreationForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password2'])
		if commit:
			user.save()
		return user

	"""def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if not password2:
			raise forms.ValidationError("You must confirm your password")
		if password1 != password2:
			raise forms.ValidationError("Your passwords do not match")
		return password2"""

class CustomUserChangeForm(UserChangeForm):
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repita su contraseña',widget=forms.PasswordInput)

	class Meta(UserChangeForm):
		model = CustomUser
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			'fecha_nacimiento',
		)
		widgets = {
			'fecha_nacimiento': CustomDateInput()
		}

	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Las contraseñas no coinciden.')
		return password2

class UserEditForm(CustomUserChangeForm):
	fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento',help_text='Ingrese la fecha en formato DD/MM/YYYY.')
	class Meta(CustomUserChangeForm):
		model = CustomUser
		fields = (
			'first_name',
			'last_name',
			'email',
			'fecha_nacimiento',
		)

	def __init__(self, *args, **kwargs):
		super(CustomUserChangeForm,self).__init__(*args,**kwargs)
		self.fields.pop('password')
		self.fields.pop('password1')
		self.fields.pop('password2')
