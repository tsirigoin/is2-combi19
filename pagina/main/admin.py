from django.contrib import admin
from .models import Combi, Insumo, Viaje, Lugar, Ruta, Comentario, Pasajero, Test

# Register your models here.
@admin.register(Combi)
class CombiAdmin(admin.ModelAdmin):
	list_display = (
		'patente',
		'tipo',
		'capacidad',
	)
@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		'descripcion',
		'precio',
		'cantidad',
	)
admin.site.register(Ruta)
admin.site.register(Viaje)
admin.site.register(Test)
admin.site.register(Lugar)
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
	list_display = (
		'usuario',
		'texto',
		'viaje',
	)
@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
	list_display = (
		'usuario',
		'estado',
		'dni',
	)
