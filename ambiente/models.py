from django.db import models
from direccion.models import Tipo_Inmueble


# Create your models here.
class Tipo_ambiente(models.Model):
    """docstring for Tipo_ambiente"""
    def __init__(self, *args, **kwargs):
        super(Tipo_ambiente, self).__init__(*args, **kwargs)

    tipo_ambiente = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_ambiente

    class Meta:
        verbose_name = "Tipo de ambiente"
        verbose_name_plural = "Tipos de ambiente"
        ordering = ["tipo_ambiente"]


class Ambiente(models.Model):
    """docstring for Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Ambiente, self).__init__(*args, **kwargs)

    ambiente = models.CharField(max_length=100)
    tipo_ambiente = models.ForeignKey(Tipo_ambiente, on_delete=models.PROTECT)

    def __str__(self):
        return self.ambiente

    class Meta:
        verbose_name = "Ambiente"
        verbose_name_plural = "Ambientes"
        ordering = ["ambiente"]


class Ambiente_Tipo_inmueble(models.Model):
    """docstring for Ambiente_Tipo_inmueble"""
    def __init__(self, *args, **kwargs):
        super(Ambiente_Tipo_inmueble, self).__init__(*args, **kwargs)

    ambiente = models.ForeignKey(Ambiente)
    tipo_inmueble = models.ForeignKey(Tipo_Inmueble)

    def __str__(self):
        return u' %s - %s' % (self.ambiente, self.tipo_inmueble)



    class Meta:
        verbose_name = "Ambiente por tipo inmueble"
        verbose_name_plural = "Ambientes por tipos de inmueble"
        ordering = ["tipo_inmueble", "ambiente"]
