from django.urls import path
from django.contrib.auth import views as auth_views
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
    path(r'accounts/perfil/membresia/contratar/',regviews.contratar_membresia,name="contratar_membresia"),
    url(r'accounts/comentarios/devolver (?P<vId>[0-9]+)', regviews.devolver_pasaje, name="devolver_pasaje"),
    url(r"^compra/(?P<vId>[0-9]+) (?P<uName>\w+)/", views.compra, name="compra"),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),name='password_reset_complete'),
    path('accounts/password_reset/',regviews.password_reset_request,name='password_reset'),
    path('accounts/perfil/editar', regviews.editar_perfil, name="editar_perfil"),
    path('accounts/perfil/cambiar_contraseña',regviews.cambiar_contraseña,name='cambiar_contraseña'),
    path('chofer',regviews.chofer,name='chofer'),
    url(r"^chofer/compra_en_persona/(?P<vId>[0-9]+) (?P<uName>\w+)/",regviews.compra_en_persona, name='compra_en_persona'),
    url(r'chofer/cancelar_viaje(?P<vId>[0-9]+)',regviews.cancelar_viaje,name='cancelar_viaje'),
    path('chofer/cancelar_viaje/cancelacion_exitosa',regviews.cancelacion_exitosa,name='cancelacion_exitosa'),
    url(r'chofer/viaje_en_curso(?P<vId>[0-9]+)',regviews.viaje_en_curso,name='viaje_en_curso'),
    url(r'chofer/finalizar_viaje(?P<vId>[0-9]+)',regviews.finalizar_viaje,name='finalizar_viaje'),
	url(r'chofer/ver_viaje(?P<vId>[0-9]+)',regviews.ver_viaje,name='ver_viaje'),
	path('chofer/ver_viaje(?P<vId>[0-9]+)/pasaje(?P<pId>[0-9]+)',regviews.pasaje_perdido,name='pasaje_perdido'),
    path('checkout/', views.checkout, name = "checkout"),
    url(r'chofer/(?P<viaje_id>[0-9]+)/cargar_test(?P<pasajero_id>[0-9]+)',regviews.test, name="test"),
    url(r'chofer/editar_test(?P<test_id>[0-9]+)',regviews.editar_test, name="editar_test"),
    url(r'chofer/eliminar_test(?P<test_id>[0-9]+)',regviews.eliminar_test, name="eliminar_test"),
    url(r'viaje/(?P<vId>[0-9]+)/ver_insumos',views.ver_insumos,name='ver_insumos'),
    path(r'viaje/(?P<pId>[0-9]+)/ver_insumos/(?P<iId>[0-9]+)',views.comprar_insumo,name='comprar_insumo'),
]
