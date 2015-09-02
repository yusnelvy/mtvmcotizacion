"""
Docstring Documentación pendiente
"""

from django.db import models
from mueble.models import Mueble
from servicio.models import Servicio


# Create your models here.
class Contenido(models.Model):
    """docstring for Contenido"""
    def __init__(self, *args, **kwargs):
        super(Contenido, self).__init__(*args, **kwargs)

    contenido = models.CharField(max_length=100, unique=True)
    densidad_baja = models.DecimalField(max_digits=7, decimal_places=2)
    densidad_media = models.DecimalField(max_digits=7, decimal_places=2)
    densidad_alta = models.DecimalField(max_digits=7, decimal_places=2)
    densidad_superalta = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.contenido

    class Meta:
        verbose_name = "contenido"
        verbose_name_plural = "contenidos"
        ordering = ['contenido']


class Contenido_Tipico(models.Model):
    """docstring for Contenido_Tipico"""
    def __init__(self, *args, **kwargs):
        super(Contenido_Tipico, self).__init__(*args, **kwargs)

    contenido = models.ForeignKey(Contenido, on_delete=models.PROTECT)
    mueble = models.ForeignKey(Mueble, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    predefinido = models.BooleanField(default=False)

    def __str__(self):
        return self.contenido

    class Meta:
        verbose_name = "Contenido Tipico"
        verbose_name_plural = "Contenidos Tipicos"
        ordering = ['mueble', 'contenido']
        unique_together = (("contenido", "mueble"),)


class Contenido_Servicio(models.Model):
    """docstring for Contenido_Servicio"""
    def __init__(self, *args, **kwargs):
        super(Contenido_Servicio, self).__init__(*args, **kwargs)

    contenido = models.ForeignKey(Contenido, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    predefinido = models.BooleanField(default=False)

    def __str__(self):
        return self.contenido

    class Meta:
        verbose_name = "Contenido Servicio"
        verbose_name_plural = "Contenidos Servicios"
        ordering = ['servicio', 'contenido']
        unique_together = (("contenido", "servicio"),)
