from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Rubro(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=50, null=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre