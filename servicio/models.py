from django.db import models


# Create your models here.
class Servicio(models.Model):
    """docstring for Servicio"""
    def __init__(self, *args, **kwargs):
        super(Servicio, self).__init__(*args, **kwargs)

    servicio = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.servicio

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['servicio']


class Material(models.Model):
    """docstring for Material"""
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args, **kwargs)

    material = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    recuperable = models.BooleanField(default=False)

    def __str__(self):
        return self.material

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        ordering = ['material']


class Servicio_Material(models.Model):
    """docstring for Servicio_Material"""
    def __init__(self, *args, **kwargs):
        super(Servicio_Material, self).__init__(*args, **kwargs)

    servicio = models.ForeignKey(Servicio)
    material = models.ForeignKey(Material)
    unique_together = ("Servicio", "Material")
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    Calculo = models.TextField(max_length=200)

    def __str__(self):
        return u' %s - %s' % (self.servicio, self.material)

    class Meta:
        verbose_name = "Material del Servicio"
        verbose_name_plural = "Materiales del Servicio"
        ordering = ['servicio', 'material']


class Complejidad(models.Model):
    """docstring for Complejidad"""
    def __init__(self, *args, **kwargs):
        super(Complejidad, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Nivel de complejidad"
        verbose_name_plural = "Niveles de complejidad"
        ordering = ['id']


class Complejidad_Servicio(models.Model):
    """docstring for Complejidad_Servicio"""
    def __init__(self, *args, **kwargs):
        super(Complejidad_Servicio, self).__init__(*args, **kwargs)

    complejidad = models.ForeignKey(Complejidad)
    tarifa = models.DecimalField(max_digits=13, decimal_places=2)
    servicio = models.ForeignKey(Servicio)

    def __str__(self):
        return self.complejidad

    class Meta:
        verbose_name = "Complejidad del Servicio"
        verbose_name_plural = "Complejidades del Servicio"
        ordering = ['servicio', 'complejidad']
