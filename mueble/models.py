from django.db import models
from ambiente.models import Ambiente


# Create your models here.
class Tipo_Mueble(models.Model):
    """docstring for Tipo_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Mueble, self).__init__(*args, **kwargs)

    tipo_mueble = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tipo_mueble

    class Meta:
        verbose_name = "Tipo mueble"
        verbose_name_plural = "Tipos muebles"


class Ocupacion(models.Model):
    """docstring for Ocupacion"""
    def __init__(self, *args, **kwargs):
        super(Ocupacion, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=2, decimal_places=2)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Ocupacion"
        verbose_name_plural = "Ocupaciones"


class Forma_Mueble(models.Model):
    """docstring for Forma_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Forma_Mueble, self).__init__(*args, **kwargs)

    forma = models.CharField(max_length=100)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Forma del Mueble"
        verbose_name_plural = "Formas del Muebles"


class Mueble(models.Model):
    """docstring for Mueble"""
    def __init__(self, *args, **kwargs):
        super(Mueble, self).__init__(*args, **kwargs)

    mueble = models.CharField(max_length=100)
    ambiente = models.ForeignKey(Ambiente)
    tipo_mueble = models.ForeignKey(Tipo_Mueble)
    forma = models.ForeignKey(Forma_Mueble)
    ocupacion = models.ForeignKey(Ocupacion)
    capacidad = models.DecimalField(max_digits=5, decimal_places=2)
    trasladable = models.BooleanField()
    apilable = models.BooleanField()
    capacidad_carga = models.BooleanField()
    capacidad_interna = models.BooleanField()

    def __unicode__(self):
        return self.mueble

    class Meta:
        verbose_name = "Mueble"
        verbose_name_plural = "Muebles"


class Tamano(models.Model):
    """docstring for Tamano"""
    def __init__(self, *args, **kwargs):
        super(Tamano, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_digits=100)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tamano"
        verbose_name_plural = "Tamanos"


class Tamano_Mueble(models.Model):
    """docstring for Tamano_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Tamano_Mueble, self).__init__(*args, **kwargs)

    tamano = models.ForeignKey(Tamano, primary_key=True)
    mueble = models.ForeignKey(Mueble, primary_key=True)
    ancho = models.DecimalField(max_digits=2, decimal_places=2)
    largo = models.DecimalField(max_digits=2, decimal_places=2)
    alto = models.DecimalField(max_digits=2, decimal_places=2)
    peso = models.DecimalField(max_digits=2, decimal_places=2)
    predefinido = models.BooleanField()

    def __unicode__(self):
        return u' %s - %s' % (self.mueble, self.tamano)

    class Meta:
        verbose_name = "Tamano mueble"
        verbose_name_plural = "Tamanos muebles"


class Mueble_Ambiente(models.Model):
    """docstring for Mueble_Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Mueble_Ambiente, self).__init__(*args, **kwargs)

    mueble = models.ForeignKey(Mueble)
    ambiente = models.ForeignKey(Ambiente)

    def __unicode__(self):
        return u' %s - %s' % (self.mueble, self.ambiente)

    class Meta:
        verbose_name = "Mueble - Ambiente"
        verbose_name_plural = "Muebles - Ambiente"
