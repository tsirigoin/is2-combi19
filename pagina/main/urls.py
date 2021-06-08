from django.urls import path
from users import views as regviews
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/registrarse/", regviews.register, name="register"),
    path('accounts/logout/', regviews.logout, name="logout"),
    path('accounts/perfil/', regviews.perfil, name="perfil"),
    url(r"^compra/(?P<vId>[0-9]+)/$", views.compra, name="compra"),
    #url(r'^search/$', views.viaje_list, name='search'),
]
