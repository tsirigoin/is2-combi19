from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def register(response):
    return render(response, "main/registro.html", {})