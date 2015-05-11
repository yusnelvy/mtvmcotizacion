from django.db import models
from cliente.models import Cliente


# Create your models here.
class Tipo_telefono(models.Model):

    tipo_telefono = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tipo_telefono

    class Meta:
        verbose_name_plural = "Tipos de telefonos"


class Telefono(models.Model):

    tipo_telefono = models.ForeignKey(Tipo_telefono, default=1)
    numero = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Telefonos"
