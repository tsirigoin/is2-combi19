from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, ValidationError
from django.db.models.constraints import UniqueConstraint
from users.models import Chofer, CustomUser
import datetime

# Create your models here.

class Combi(models.Model):
    patente = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(6)])
    tipo = models.CharField(choices={('comoda','Comoda'),('super comoda', 'Super Comoda')},max_length=12)
    capacidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.patente

class Insumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    cantidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.nombre

class Lugar(models.Model):
    localidad = models.CharField(max_length=150)
    provincia = models.CharField(max_length=100)

    class Meta:
        unique_together = ('localidad', 'provincia',)

    def __str__(self):
        return (self.localidad+", "+self.provincia)

class Ruta(models.Model):
    origen = models.ForeignKey(Lugar, default=None, on_delete=models.CASCADE, related_name='origen')
    destino = models.ForeignKey(Lugar, default=None, on_delete=models.CASCADE, related_name='destino')

    class Meta:
        unique_together = ('origen', 'destino')

    def clean(self, *args, **kwargs):
        ori = self.origen
        des = self.destino
        if ori == des:
            raise ValidationError("Origen y destino no pueden ser iguales")
        return


    def save(self, *args, **kwargs):
        self.full_clean()
        super(Ruta, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.origen)+" - "+str(self.destino)

class Comentario(models.Model):
    usuario = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)
    texto = models.CharField(max_length=100)

    def __str__(self):
        return (str(self.usuario)+" "+(self.texto))

class Pasajero(models.Model):
    usuario = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)
    estado = models.CharField(choices={('reservado','Reservado'),('viajando','Viajando'),('finalizado','Finalizado')},max_length=12)

    def __str__(self):
        return (str(self.usuario)+" "+(self.estado))

class Viaje(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField(validators=[MinValueValidator(datetime.date.today()+datetime.timedelta(hours=24))])
    hora = models.TimeField(default=None)
    ruta =  models.ForeignKey(Ruta, default=None, on_delete=models.CASCADE)
    chofer = models.ForeignKey(Chofer, default=None, on_delete=models.CASCADE)
    combi =  models.ForeignKey(Combi, default=None, on_delete=models.CASCADE)
    precio = models.DecimalField(default=None, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    insumo = models.ManyToManyField(Insumo,blank=True)
    pasajeros = models.ManyToManyField(Pasajero, blank=True)
    comentarios = models.ManyToManyField(Comentario, blank=True)

    class Meta:
        unique_together = ('chofer', 'fecha','hora', 'ruta',)

    def __str__(self):
        return (self.descripcion+" "+str(self.ruta)+" "+str(self.fecha))
