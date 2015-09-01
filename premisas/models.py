from django.db import models


# Create your models here.
class Empresa(models.Model):
    empresa = models.CharField(max_length=250)
    telefonos = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    sitio_web = models.URLField()
    correo = models.EmailField()
    responsable = models.CharField(max_length=250, null=True, blank=True)
    cuit = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='static/image/')
