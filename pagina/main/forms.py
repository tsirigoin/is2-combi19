from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Comentario


class CustomComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = (
            'usuario',
			'texto',
            'viaje'
		)
