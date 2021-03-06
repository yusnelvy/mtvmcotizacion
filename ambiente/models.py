from django.db import models
from direccion.models import Tipo_Inmueble


# Create your models here.

class Ambiente(models.Model):
    """docstring for Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Ambiente, self).__init__(*args, **kwargs)

    ambiente = models.CharField(max_length=100)

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

    ambiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT)
    tipo_inmueble = models.ForeignKey(Tipo_Inmueble, on_delete=models.PROTECT)

    def __str__(self):
        return u' %s - %s' % (self.ambiente, self.tipo_inmueble)

    class Meta:
        verbose_name = "Ambiente por tipo inmueble"
        verbose_name_plural = "Ambientes por tipos de inmueble"
        ordering = ["tipo_inmueble", "ambiente"]
        unique_together = (("ambiente", "tipo_inmueble"),)
