from django.db import models


class models_producto(models.Model):
    nombre=models.CharField(max_length=80)
    precio=models.IntegerField()
    def __str__(self):
        return f"nombre: {self.nombre}////precio: {self.precio}"

