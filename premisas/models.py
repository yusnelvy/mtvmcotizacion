from django.db import models


# Create your models here.
class Empresa(models.Model):
    """docstring for Empresa"""
    empresa = models.CharField(max_length=250)
    telefonos = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    sitio_web = models.URLField()
    correo = models.EmailField()
    responsable = models.CharField(max_length=250, null=True, blank=True)
    cuit = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='static/img/')


class FuentePromocion(models.Model):
    """docstring for FuentePromocion"""
    fuente_promocion = models.CharField(max_length=100)

    def __str__(self):
        return self.fuente_promocion
