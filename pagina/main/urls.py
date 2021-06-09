from django.urls import path
from users import views as regviews
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/registrarse/", regviews.register, name="register"),
    path('accounts/logout/', regviews.logout, name="logout"),
    path('accounts/perfil/', regviews.perfil, name="perfil"),
    url(r'^search/$', views.viaje_list, name='search'),
    path('accounts/comentarios/', regviews.comentarios, name="comentario"),
    #path('guardarComentario', regviews.crear_comentario, name="viaje"),

]
