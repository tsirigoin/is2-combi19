from django.contrib import admin
from .models import Combi, Insumo, Viaje, Lugar, Ruta, Comentario, Pasajero

# Register your models here.
admin.site.register(Combi)
admin.site.register(Insumo)
admin.site.register(Ruta)
admin.site.register(Viaje)
admin.site.register(Lugar)
admin.site.register(Comentario)
admin.site.register(Pasajero)
