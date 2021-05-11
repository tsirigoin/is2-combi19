from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, int_list_validator,ValidationError
import datetime
from users.models import Chofer

# Create your models here.

class Combi(models.Model):
    patente = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(6)])
    tipo = models.CharField(choices={('chico','Chico'),('mediano', 'Mediano'),('grande','Grande')},max_length=10)
    capacidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):  
        return self.patente

class Insumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
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
    fecha = models.DateField(validators=[MinValueValidator(datetime.date.today()+datetime.timedelta(hours=24))])
    hora = models.TimeField(default=None)
    ruta =  models.ForeignKey(Ruta, default=None, on_delete=models.CASCADE)
    chofer =  models.ForeignKey(Chofer, default=None, on_delete=models.CASCADE)
    combi =  models.ForeignKey(Combi, default=None, on_delete=models.CASCADE)
    precio = models.DecimalField(default=None, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    insumo = models.ManyToManyField(Insumo,blank=True)

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