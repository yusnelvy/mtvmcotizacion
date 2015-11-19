from django.db import models
from ambiente.models import Ambiente
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Tipo_Mueble(models.Model):
    """docstring for Tipo_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Mueble, self).__init__(*args, **kwargs)

    tipo_mueble = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tipo_mueble

    class Meta:
        verbose_name = "Tipo mueble"
        verbose_name_plural = "Tipos de mueble"
        ordering = ['tipo_mueble']


class Ocupacion(models.Model):
    """docstring for Ocupacion"""
    def __init__(self, *args, **kwargs):
        super(Ocupacion, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100, unique=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2,
                                validators=[
                                    MaxValueValidator(100),
                                    MinValueValidator(0)
                                ])

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Ocupacion"
        verbose_name_plural = "Ocupaciones"
        ordering = ['id']


class Forma_Mueble(models.Model):
    """docstring for Forma_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Forma_Mueble, self).__init__(*args, **kwargs)

    forma = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.forma

    class Meta:
        verbose_name = "Forma del Mueble"
        verbose_name_plural = "Formas del Mueble"
        ordering = ['forma']


class Mueble(models.Model):
    """docstring for Mueble"""
    def __init__(self, *args, **kwargs):
        super(Mueble, self).__init__(*args, **kwargs)

    mueble = models.CharField(max_length=100, unique=True)
    tipo_mueble = models.ForeignKey(Tipo_Mueble, on_delete=models.PROTECT)
    forma = models.ForeignKey(Forma_Mueble, on_delete=models.PROTECT)
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.PROTECT)
    capacidad = models.DecimalField(max_digits=8, decimal_places=3,
                                    validators=[
                                        MaxValueValidator(100),
                                        MinValueValidator(0)
                                    ])
    trasladable = models.BooleanField(default=None)
    apilable = models.BooleanField(default=None)
    capacidad_carga = models.BooleanField(default=None)
    capacidad_interna = models.BooleanField(default=None)

    def __str__(self):
        return self.mueble

    class Meta:
        verbose_name = "Mueble"
        verbose_name_plural = "Muebles"
        ordering = ['mueble']


class Tamano(models.Model):
    """docstring for Tamano"""
    def __init__(self, *args, **kwargs):
        super(Tamano, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tamano"
        verbose_name_plural = "Tamanos"
        ordering = ['id']


class Densidad(models.Model):
    """docstring for Densidad"""
    def __init__(self, *args, **kwargs):
        super(Densidad, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Densidad"
        verbose_name_plural = "Densidades"
        ordering = ['id']


class Tamano_Mueble(models.Model):
    """docstring for Tamano_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Tamano_Mueble, self).__init__(*args, **kwargs)

    tamano = models.ForeignKey(Tamano, on_delete=models.PROTECT, default=1)
    mueble = models.ForeignKey(Mueble, on_delete=models.PROTECT)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.mueble, self.tamano)

    def _get_volumenmueble(self):
        return round((self.ancho*self.alto*self.largo)/1000000, 3)
    volumenmueble = property(_get_volumenmueble)

    class Meta:
        verbose_name = "Tamano del mueble"
        verbose_name_plural = "Tamanos del mueble"
        ordering = ['mueble', 'tamano']
        unique_together = (("tamano", "mueble"),)


class Mueble_Ambiente(models.Model):
    """docstring for Mueble_Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Mueble_Ambiente, self).__init__(*args, **kwargs)

    mueble = models.ForeignKey(Mueble, on_delete=models.PROTECT)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.mueble, self.ambiente)

    class Meta:
        verbose_name = "Mueble del Ambiente"
        verbose_name_plural = "Muebles  del Ambiente"
        ordering = ['ambiente', 'mueble']
        unique_together = (("mueble", "ambiente"),)
