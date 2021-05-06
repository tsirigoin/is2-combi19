from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class chofer(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200)
    informacion_contacto = models.CharField(max_length=200)

    def __str__(self):
        return (self.nombre+" "+self.apellido)


class combi(models.Model):
    patente = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.patente

class insumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    cantidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])

    def __str__(self):
        return self.nombre+" "+self.descripcion

class ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

    class Meta:
        unique_together = ('origen', 'destino',)

    def __str__(self):
        return self.origen+" "+self.destino

class viaje(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    ruta =  models.ForeignKey(ruta, default=None, on_delete=models.CASCADE)
    chofer =  models.ForeignKey(chofer, default=None, on_delete=models.CASCADE)
    combi =  models.ForeignKey(combi, default=None, on_delete=models.CASCADE)
    insumo = models.ForeignKey(insumo, default=None, on_delete=models.CASCADE) #falta correguir

    class Meta:
        unique_together = ('chofer', 'fecha', 'ruta',)

    def __str__(self):
        return (self.descripcion+" "+self.ruta.origen+" "+self.ruta.destino+" "+str(self.fecha))

class lugar(models.Model):
    localidad = models.CharField(max_length=150)
    provincia = models.CharField(max_length=100)

    class Meta:
        unique_together = ('localidad', 'provincia',)

    def __str__(self):
        return (self.localidad+" "+self.provincia)

class usuario(models.Model):
    mail = models.EmailField()
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechaNac = models.DateField()

    def __str__(self):
        return (self.nombre+" "+self.apellido)
