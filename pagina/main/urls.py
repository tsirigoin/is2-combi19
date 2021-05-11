from django.urls import path
from users import views as regviews
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registrarse/", regviews.register, name="register"),
]