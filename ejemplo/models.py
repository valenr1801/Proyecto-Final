from django.db import models
#FAMILIA
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento= models.CharField(max_length=200)
def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id},{self.fecha_nacimiento}"
#MASCOTA
class Mascota(models.Model):
    propietario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
def __str__(self):
      return f"{self.propietario},{self.nombre},{self.raza}"

#AUTO
class Auto(models.Model):
    propietario = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
def __str__(self):
      return f"{self.propietario},{self.modelo}"
