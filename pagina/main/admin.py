from django.contrib import admin
from .models import combi,chofer,insumo, viaje, lugar,ruta

# Register your models here.
admin.site.register(combi)
admin.site.register(chofer)
admin.site.register(insumo)
admin.site.register(ruta)
admin.site.register(viaje)
admin.site.register(lugar)
