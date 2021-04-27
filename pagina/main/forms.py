from django import forms

class CreateNewUser(forms.Form):
	nombre = forms.CharField(label="Nombre", max_length=100)
	apellido = forms.CharField(label="Apellido", max_length=100)
	