from django.db import models


# Create your models here.
class Estado(models.Model):
    """docstring for Estado"""
    estado = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"
        ordering = ['id']


class EstadoDocumento(models.Model):
    """docstring"""
    estado = models.ForeignKey(Estado)
    orden = models.IntegerField()
    documento = models.CharField(max_length=100)

    def __str__(self):
        return u' %s - %s' % (self.estado, self.documento)

    class Meta:
        verbose_name = "Estado de documento"
        verbose_name_plural = "Estados de documentos"
        ordering = ['estado', 'documento']
