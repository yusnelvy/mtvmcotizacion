from django.db import models
from mueble.models import Mueble


# Create your models here.
class Contenedor(models.Model):
    """docstring for Contenedor"""
    def __init__(self, *args, **kwargs):
        super(Contenedor, self).__init__(*args, **kwargs)

    contenedor = models.CharField(max_length=100, unique=True)
    capacidad_volumen = models.DecimalField(max_digits=5, decimal_places=2)
    capacidad_peso = models.DecimalField(max_digits=5, decimal_places=2)
    volumen_contenedor = models.DecimalField(max_digits=5, decimal_places=2)
    peso_contenedor = models.DecimalField(max_digits=5, decimal_places=2)
    retornable = models.BooleanField(default=None)

    def __str__(self):
        return self.contenedor

    class Meta:
        verbose_name = "contenedor"
        verbose_name_plural = "contenedores"


class Contenido(models.Model):
    """docstring for Contenido"""
    def __init__(self, *args, **kwargs):
        super(Contenido, self).__init__(*args, **kwargs)

    contenido = models.CharField(max_length=100, unique=True)
    contenedor = models.ForeignKey(Contenedor)
    densidad_baja = models.DecimalField(max_digits=5, decimal_places=2)
    densidad_media = models.DecimalField(max_digits=5, decimal_places=2)
    densidad_alta = models.DecimalField(max_digits=5, decimal_places=2)
    densidad_superalta = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.contenido

    class Meta:
        verbose_name = "contenido"
        verbose_name_plural = "contenidos"


class Contenido_Tipico(models.Model):
    """docstring for Contenido_Tipico"""
    def __init__(self, *args, **kwargs):
        super(Contenido_Tipico, self).__init__(*args, **kwargs)

    contenido = models.ForeignKey(Contenido)
    mueble = models.ForeignKey(Mueble)
    cantidad = models.DecimalField(max_digits=2, decimal_places=2)
    unique_together = ("Contenido", "Mueble")

    def __str__(self):
        return self.contenido

    class Meta:
        verbose_name = "Contenido Tipico"
        verbose_name_plural = "Contenidos Tipicos"
