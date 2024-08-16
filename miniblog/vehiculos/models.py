from django.db import models
from datetime import date, datetime

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

#Marca,Modelo,Año de Fabricacion,Cantidad de Puertas,Cilindrada,Tipo de Combustible,Pais de Fabricacion,Precio en dolares

class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    fabricado_el = models.IntegerField(default=datetime.now().year)
    cantidad_puertas = models.IntegerField()
    cilindrada = models.FloatField()
    tipo_combustible = models.CharField(max_length=50)
    pais_fabricacion = models.CharField(max_length=50)
    precio_dolares = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} {self.fabricado_el}"
