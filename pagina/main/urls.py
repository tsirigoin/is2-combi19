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
    path('accounts/comentarios/<viaje_id>/', regviews.comentarios, name="comentario"),
    path(r'accounts/comentarios/eliminar/<comentario_id>/', regviews.eliminar_comentario, name="eliminarcomentario"),
    path(r'accounts/comentarios/editar/<comentario_id>', regviews.modificar_comentario, name="editarcomentario"),
    path(r'accounts/perfil/membresia/cambiar/',regviews.cambiar_membresia,name="cambiar_membresia"),
    url(r"^compra/(?P<vId>[0-9]+) (?P<uName>\w+)/", views.compra, name="compra")
]
    