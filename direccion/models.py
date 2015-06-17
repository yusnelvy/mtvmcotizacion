"""
docstring

Documentacion del proyecto

"""
from django.db import models
from cliente.models import Cliente
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
class Pais(models.Model):
    """docstring for Pais"""
    def __init__(self, *args, **kwargs):
        super(Pais, self).__init__(*args, **kwargs)

    pais = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.pais

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['pais']


class Provincia(models.Model):
    """docstring for Provincia"""
    def __init__(self, *args, **kwargs):
        super(Provincia, self).__init__(*args, **kwargs)

    provincia = models.CharField(max_length=100, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return self.provincia

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ['pais', 'provincia']


class Ciudad(models.Model):
    """docstring for Ciudad"""
    def __init__(self, *args, **kwargs):
        super(Ciudad, self).__init__(*args, **kwargs)

    ciudad = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)

    def __str__(self):
        return self.ciudad

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['provincia', 'ciudad']


class Zona(models.Model):
    """docstring for Zona"""
    def __init__(self, *args, **kwargs):
        super(Zona, self).__init__(*args, **kwargs)

    zona = models.CharField(max_length=100, unique=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)

    def __str__(self):
        return self.zona

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"
        ordering = ['ciudad', 'zona']


class Tipo_direccion(models.Model):
    """docstring for Tipo_direccion"""
    def __init__(self, *args, **kwargs):
        super(Tipo_direccion, self).__init__(*args, **kwargs)

    tipo_direccion = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_direccion

    class Meta:
        verbose_name = "Tipo de direccion"
        verbose_name_plural = "Tipos de direccion"
        ordering = ['tipo_direccion']


class Direccion(models.Model):
    """docstring for Direccion"""
    def __init__(self, *args, **kwargs):
        super(Direccion, self).__init__(*args, **kwargs)

    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    piso = models.CharField(max_length=100)
    adicional = models.CharField(max_length=250, blank=True)
    tipo_direccion = models.ForeignKey(Tipo_direccion, on_delete=models.PROTECT)
    pais = models.ForeignKey(Pais)
    provincia = ChainedForeignKey(Provincia, chained_field='pais', chained_model_field='pais')
    ciudad = ChainedForeignKey(Ciudad, chained_field='provincia', chained_model_field='provincia')
    zona = ChainedForeignKey(Zona, chained_field='ciudad', chained_model_field='ciudad')
    zip1 = models.CharField(max_length=100)
    punto_referencia = models.CharField(max_length=250)
    cliente = models.ForeignKey(Cliente)

    def __str__(self):

        return u' %s - %s - %s' % (self.calle, self.numero, self.piso)

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
        ordering = ['tipo_direccion']


class Tipo_Inmueble(models.Model):
    """docstring for Tipo_Inmueble"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Inmueble, self).__init__(*args, **kwargs)

    tipo_inmueble = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_inmueble

    class Meta:
        verbose_name = "Tipo de inmueble"
        verbose_name_plural = "Tipos de inmueble"
        ordering = ['tipo_inmueble']


class Complejidad_Inmueble(models.Model):
    """docstring for Complejidad_Inmueble"""
    def __init__(self, *args, **kwargs):
        super(Complejidad_Inmueble, self).__init__(*args, **kwargs)

    complejidad = models.CharField(max_length=100, unique=True)
    factor = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.complejidad

    class Meta:
        verbose_name = "complejidad del inmueble"
        verbose_name_plural = "complejidades del inmueble"
        #ordering = ['complejidad']


class Tarifa_valor(models.Model):
    """docstring for Tarifa_valor"""
    def __init__(self, *args, **kwargs):
        super(Tarifa_valor, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100, unique=True)
    valor = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tarifa del inmueble"
        verbose_name_plural = "Tarifas del inmueble"
        ordering = ['descripcion']


class Inmueble(models.Model):
    """docstring for Inmueble"""
    def __init__(self, *args, **kwargs):
        super(Inmueble, self).__init__(*args, **kwargs)

    inmueble = models.CharField(max_length=100)
    tipo_inmueble = models.ForeignKey(Tipo_Inmueble, on_delete=models.PROTECT)
    direccion = models.ForeignKey(Direccion, on_delete=models.PROTECT)
    numero_ambientes = models.IntegerField()
    pisos = models.IntegerField()
    pisos_escalera = models.IntegerField()
    rampa = models.BooleanField(default=False)
    ascensor = models.BooleanField(default=False)
    ascensor_servicio = models.BooleanField(default=False)
    pisos_ascensor_servicio = models.IntegerField()
    pisos_ascensor = models.IntegerField()
    complejidad = models.ForeignKey(Complejidad_Inmueble, on_delete=models.PROTECT)
    distancia_vehiculo = models.IntegerField()
    tarifa_valor = models.ForeignKey(Tarifa_valor, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.inmueble)

    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"
        ordering = ['inmueble']


class locaciones(models.Model):
    pais = models.ForeignKey(Pais)
    provincia = ChainedForeignKey(Provincia, chained_field='pais', chained_model_field='pais')
    ciudad = ChainedForeignKey(Ciudad, chained_field='provincia', chained_model_field='provincia')
    zona = ChainedForeignKey(Zona, chained_field='ciudad', chained_model_field='ciudad')
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.direccion)
