from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class chofer(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=200)
    informacion_contacto = models.CharField(max_length=200)

    def __str__(self):
        return (self.nombre+self.apellido)


class combi(models.Model):
    patente = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.patente