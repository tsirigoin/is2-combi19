from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Chofer

# Create your models here.

class Combi(models.Model):
    patente = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.patente

class Insumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    cantidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.nombre+" "+self.descripcion

class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

    class Meta:
        unique_together = ('origen', 'destino',)

    def __str__(self):
        return self.origen+" "+self.destino

class Viaje(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    ruta =  models.ForeignKey(Ruta, default=None, on_delete=models.CASCADE)
    chofer =  models.ForeignKey(Chofer, default=None, on_delete=models.CASCADE)
    combi =  models.ForeignKey(Combi, default=None, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, default=None, on_delete=models.CASCADE) #falta correguir

    class Meta:
        unique_together = ('chofer', 'fecha', 'ruta',)

    def __str__(self):
        return (self.descripcion+" "+self.ruta.origen+" "+self.ruta.destino+" "+str(self.fecha))

class Lugar(models.Model):
    localidad = models.CharField(max_length=150)
    provincia = models.CharField(max_length=100)

    class Meta:
        unique_together = ('localidad', 'provincia',)

    def __str__(self):
        return (self.localidad+" "+self.provincia)