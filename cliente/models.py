from django.db import models


# Create your models here.
class Cliente(models.Model):
    """docstring for Cliente"""
    def __init__(self, *args, **kwargs):
        super(Cliente, self).__init__(*args, **kwargs)

    nombre_principal = models.CharField(max_length=250)
    comentarios = models.TextField(blank=True)
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre_principal

    class Meta:
        verbose_name_plural = "Clientes"


class Email(models.Model):

    email = models.EmailField()
    cliente = models.ForeignKey(Cliente, default=1)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Emails"
