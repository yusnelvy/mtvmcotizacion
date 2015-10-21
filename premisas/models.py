from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.empresa


class FuentePromocion(models.Model):
    """docstring for FuentePromocion"""
    fuente_promocion = models.CharField(max_length=100)

    def __str__(self):
        return self.fuente_promocion


class PerzonalizacionVisual(models.Model):
    """docstring for PerzonalizacionVisual"""
    usuario = models.ForeignKey(User)
    tipo = models.CharField(max_length=250)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return u' %s - %s' % (self.usuario, self.tipo)

    class Meta:
        verbose_name = "Perzonalización Visual"
        verbose_name_plural = "Perzonalizaciones Visuales"
        unique_together = (("usuario", "tipo"),)
