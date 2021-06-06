from django.shortcuts import render, redirect
from django.contrib.auth import logout as logoutFunct
from .forms import CustomUserCreationForm, CustomUserEditForm

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
	user_form = CustomUserEditForm(instance=response.user)
	return render(response,'users/perfil.html',{'user': response.user,
		'user_form': user_form,
	})