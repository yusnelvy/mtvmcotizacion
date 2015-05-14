from django.db import models


# Create your models here.
class Servicio(models.Model):
    """docstring for Servicio"""
    def __init__(self, *args, **kwargs):
        super(Servicio, self).__init__(*args, **kwargs)

    servicio = models.CharField(max_length=100)

    def __unicode__(self):
        return self.servicio

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"


class Material(models.Model):
    """docstring for Material"""
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args, **kwargs)

    material = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    recuperable = models.BooleanField()

    def __unicode__(self):
        return self.material

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"


class Servicio_Material(models.Model):
    """docstring for Servicio_Material"""
    def __init__(self, *args, **kwargs):
        super(Servicio_Material, self).__init__(*args, **kwargs)

    servicio = models.ForeignKey(Servicio, primary_key=True)
    material = models.ForeignKey(Material, primary_key=True)

    def __unicode__(self):
        return u' %s - %s' % (self.servicio, self.material)

    class Meta:
        verbose_name = "Servicio Material"
        verbose_name_plural = "Servicios Materiales"


class Complejidad(models.Model):
    """docstring for Complejidad"""
    def __init__(self, *args, **kwargs):
        super(Complejidad, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Complejidad"
        verbose_name_plural = "Complejidades"


class Complejidad_Servicio(models.Model):
    """docstring for Complejidad"""
    def __init__(self, *args, **kwargs):
        super(Complejidad, self).__init__(*args, **kwargs)

    complejidad = models.ForeignKey(Complejidad)
    tarifa = models.DecimalField(max_digits=13, decimal_places=2)
    servicio = models.ForeignKey(Servicio)

    def __unicode__(self):
        return self.complejidad

    class Meta:
        verbose_name = "Complejidad_Servicio"
        verbose_name_plural = "Complejidad_Servicios"
