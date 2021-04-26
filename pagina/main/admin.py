from django.contrib import admin
from .models import combi,chofer,insumo, viaje

# Register your models here.
admin.site.register(combi)
admin.site.register(chofer)
admin.site.register(insumo)
admin.site.register(viaje)