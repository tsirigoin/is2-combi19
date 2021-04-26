from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class chofer(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=200)
    informacion_contacto = models.CharField(max_length=200)

    def __str__(self):
        return (self.nombre+" "+self.apellido)


class combi(models.Model):
    patente = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.patente

class insumo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    cantidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.nombre+" "+self.descripcion

class viaje(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    lugar_salida = models.CharField(max_length=100)
    lugar_llegada = models.CharField(max_length=100)
    chofer =  models.ForeignKey(chofer, default=None, on_delete=models.CASCADE)
    combi =  models.ForeignKey(combi, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return (self.lugar_salida+" "+self.lugar_salida+" "+self.fecha)

class lugar(models.Model):
    localidad = models.CharField(max_length=150)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return (self.localidad+" "+self.provincia)
