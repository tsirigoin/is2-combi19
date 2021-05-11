from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

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