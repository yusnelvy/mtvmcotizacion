from django.db import models
from cliente.models import Cliente


# Create your models here.
class Tipo_telefono(models.Model):
    """docstring for Tipo_telefono"""
    def __init__(self, *args, **kwargs):
        super(Tipo_telefono, self).__init__(*args, **kwargs)

    tipo_telefono = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tipo_telefono

    class Meta:
        verbose_name_plural = "Tipos de telefonos"


class Telefono(models.Model):

    tipo_telefono = models.ForeignKey(Tipo_telefono, default=1, on_delete=models.PROTECT)
    numero = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Telefonos"
