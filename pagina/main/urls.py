from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registrarse", views.register, name="registro")
]