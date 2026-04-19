from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Regla(models.Model):
    monto_minimo = models.FloatField()
    porcentaje = models.FloatField()


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha = models.DateField()
