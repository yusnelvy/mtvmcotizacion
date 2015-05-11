from django.db import models
from cliente import Cliente


# Create your models here.
class Pais(models.Model):
    """docstring for Pais"""
    def __init__(self, *args, **kwargs):
        super(Pais, self).__init__(*args, **kwargs)

    pais = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return self.pais

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"


class Provincia(models.Model):
    """docstring for Provincia"""
    def __init__(self, *args, **kwargs):
        super(Provincia, self).__init__(*args, **kwargs)

    provincia = models.CharField(max_length=100, unique=True)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
        return self.provincia

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"


class Ciudad(models.Model):
    """docstring for Ciudad"""
    def __init__(self, *args, **kwargs):
        super(Ciudad, self).__init__(*args, **kwargs)

    ciudad = models.CharField(max_length=100, unique=True)
    provincia = models.ForeignKey(Provincia)

    def __unicode__(self):
        return self.ciudad

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class Zona(models.Model):
    """docstring for Zona"""
    def __init__(self, *args, **kwargs):
        super(Zona, self).__init__(*args, **kwargs)

    zona = models.CharField(max_length=100, unique=True)
    cuidad = models.ForeignKey(Ciudad)

    def __unicode__(self):
        return self.zona

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"


class Tipo_direccion(models.Model):
    """docstring for Tipo_direccion"""
    def __init__(self, *args, **kwargs):
        super(Tipo_direccion, self).__init__(*args, **kwargs)

    tipo_direccion = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_direccion

    class Meta:
        verbose_name = "Tipo de direccion"
        verbose_name_plural = "Tipos de direccion"


class Direccion(models.Model):
    """docstring for Direccion"""
    def __init__(self, *args, **kwargs):
        super(Direccion, self).__init__(*args, **kwargs)

    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    piso = models.CharField(max_length=100)
    adicional = models.CharField(max_length=250)
    tipo_direccion = models.ForeignKey(Tipo_direccion)
    zona = models.ForeignKey(Zona)
    zip1 = models.CharField(max_length=100)
    punto_referencia = models.CharField(max_length=250)
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
        return self.direccion

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"


class Tipo_Inmueble(object):
    """docstring for Tipo_Inmueble"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Inmueble, self).__init__(*args, **kwargs)

    tipo_inmueble = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tipo_inmueble

    class Meta:
        verbose_name = "Tipo inmueble"
        verbose_name_plural = "Tipo inmuebles"


class Complejidad_Inmueble(models.Model):
    """docstring for Complejidad_Inmueble"""
    def __init__(self, *args, **kwargs):
        super(Complejidad_Inmueble, self).__init__(*args, **kwargs)

    complejidad = models.CharField(max_length=100)
    factor = models.DecimalField(max_digits=2, decimal_places=2)

    def __unicode__(self):
        return self.complejidad

    class Meta:
        verbose_name = "complejidad del inmueble"
        verbose_name_plural = "complejidades del inmuebles"


class Inmueble(models.Model):
    """docstring for Inmueble"""
    def __init__(self, *args, **kwargs):
        super(Inmueble, self).__init__(*args, **kwargs)

    inmueble = models.CharField(max_length=100)
    tipo_inmueble = models.ForeignKey(Tipo_Inmueble)
    direccion = models.ForeignKey(Direccion)
    numero_ambientes = models.IntegerField()
    pisos = models.IntegerField()
    pisos_escalera = models.IntegerField()
    rampa = models.BooleanField()
    ascensor = models.BooleanField()
    ascensor_servicio = models.BooleanField()
    pisos_ascensor_servicio = models.IntegerField()
    pisos_ascensor = models.IntegerField()
    complejidad = models.ForeignKey(Complejidad_Inmueble)
    distancia_vehiculo = models.IntegerField()

    def __unicode__(self):
        return self.inmueble

    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"
