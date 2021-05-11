from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repita su contraseña',widget=forms.PasswordInput)
	accept = forms.BooleanField(label="Acepto los Términos y Condiciones")
	
	class Meta(UserCreationForm):
		model = CustomUser
		fields = (
			'username',
			'email',
			'password1',
			'password2',
			'fecha_nacimiento',
			'accept',
		)
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

class CustomUserChangeForm(UserChangeForm):
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repita su contraseña',widget=forms.PasswordInput)
	
	class Meta(UserChangeForm):
		model = CustomUser
		fields = (
			'username',
			'email',
			'password1',
			'password2',
			'fecha_nacimiento',
		)
	
	def clean_password(self):
		return self.initial['password']