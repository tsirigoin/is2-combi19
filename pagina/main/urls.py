from django.urls import path
from users import views as regviews
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/registrarse/", regviews.register, name="register"),
    path('accounts/logout/', regviews.logout, name="logout"),
    path('accounts/perfil/', regviews.perfil, name="perfil"),
]
