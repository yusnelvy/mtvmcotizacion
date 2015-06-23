# -*- encoding: utf-8 -*-
from django.db import models
from direccion.models import Inmueble
from cliente.models import Cliente
from trabajador.models import Cargo_trabajador
from ambiente.models import Ambiente
from mueble.models import Mueble
from servicio.models import Servicio, Material
from contenido.models import Contenido
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Estado_Cotizacion(models.Model):
    """docstring for Estado_Cotizacion"""
    def __init__(self, *args, **kwargs):
        super(Estado_Cotizacion, self).__init__(*args, **kwargs)

    estado = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"
        ordering = ['id']


class Tiempo_Carga(models.Model):
    """docstring for Tiempo_Carga"""
    def __init__(self, *args, **kwargs):
        super(Tiempo_Carga, self).__init__(*args, **kwargs)

    tiempo_carga = models.TimeField()
    volumen_min = models.DecimalField(max_digits=13, decimal_places=2, blank=True,
                                      default=0.00, validators=[MinValueValidator(0.01)])
    volumen_max = models.DecimalField(max_digits=13, decimal_places=2, blank=True, default=0.00,
                                      validators=[MaxValueValidator(100), MinValueValidator(1)])
    nro_objeto_min = models.PositiveIntegerField(validators=[MaxValueValidator(100),
                                                             MinValueValidator(1)])
    nro_objeto_max = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    peso_min = models.DecimalField(max_digits=13, decimal_places=2, blank=True, default=0.00)
    peso_max = models.DecimalField(max_digits=13, decimal_places=2, blank=True, default=0.00)
    cantidad_trabajador = models.PositiveIntegerField(validators=[MaxValueValidator(20), MinValueValidator(1)])

    def __str__(self):
        return str(self.tiempo_carga)

    class Meta:
        verbose_name = "tiempo de carga"
        verbose_name_plural = "tiempos de carga"
        ordering = ['tiempo_carga']


class Piso(models.Model):
    """docstring for Piso"""
    def __init__(self, *args, **kwargs):
        super(Piso, self).__init__(*args, **kwargs)

    piso = models.CharField(max_length=100, unique=True)
    factor = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.piso

    class Meta:
        verbose_name = "piso"
        verbose_name_plural = "pisos"
        ordering = ['piso']


class Cotizacion(models.Model):
    """docstring for Cotizacion"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion, self).__init__(*args, **kwargs)

    numero_contrato = models.CharField(max_length=100, unique=True)
    estado = models.ForeignKey(Estado_Cotizacion)
    numero_cotizacion = models.CharField(max_length=100, unique=True)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    creadopor = models.ForeignKey(User, related_name="creadopor")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(blank=True)
    cotizador = models.ForeignKey(User, related_name="cotizador")
    fecha_estimadamudanza = models.DateTimeField()
    cantidad_ambientes = models.PositiveIntegerField(blank=True, default=0)
    cantidad_muebles = models.PositiveIntegerField(blank=True, default=0)
    volumen_muebles_sugerido = models.DecimalField(max_digits=5, decimal_places=2,
                                                   blank=True, default=0.00)
    volumen_muebles_cotizado = models.DecimalField(max_digits=5, decimal_places=2,
                                                   blank=True, default=0.00)
    peso_muebles = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00)
    cantidad_contenedores = models.PositiveIntegerField(blank=True, default=0)
    peso_contenedores = models.DecimalField(max_digits=7, decimal_places=2,
                                            blank=True, default=0.00)
    volumen_contenedores = models.DecimalField(max_digits=7, decimal_places=2,
                                               blank=True, default=0.00)
    peso_contenidos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00)
    volumen_contenidos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00)
    peso_materiales = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00)
    monto_muebles = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    monto_material = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    monto_descuento = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    total_sin_impuesto = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    monto_impuesto = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    total_con_impuesto = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    tiempo_carga = models.TimeField()
    total_recorrido_tiempo = models.TimeField()
    total_recorrido_km = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)

    def __str__(self):
        return self.numero_contrato

    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"
        ordering = ['numero_contrato']


class Vehiculo(models.Model):
    """docstring for Vehiculo"""
    def __init__(self, *args, **kwargs):
        super(Vehiculo, self).__init__(*args, **kwargs)

    modelo = models.CharField(max_length=100, unique=True)
    tarifa_hora = models.DecimalField(max_digits=7, decimal_places=2)
    tarifa_recorrido = models.DecimalField(max_digits=7, decimal_places=2)
    capacidad_volumen = models.DecimalField(max_digits=7, decimal_places=2)
    capacidad_peso = models.DecimalField(max_digits=7, decimal_places=2)
    cargo = models.ForeignKey(Cargo_trabajador)

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        ordering = ['-tarifa_hora']


class Vehiculo_Cotizacion(models.Model):
    """docstring for Vehiculo_Cotizacion"""
    def __init__(self, *args, **kwargs):
        super(Vehiculo_Cotizacion, self).__init__(*args, **kwargs)

    vehiculo = models.ForeignKey(Vehiculo)
    cotizacion = models.ForeignKey(Cotizacion)
    cantidad = models.PositiveIntegerField()
    cantidad_hora = models.TimeField()
    tarifa_hora = models.DecimalField(max_digits=7, decimal_places=2)
    costo_hora = models.DecimalField(max_digits=7, decimal_places=2)
    recorrido = models.DecimalField(max_digits=7, decimal_places=2)
    tarifa_recorrido = models.DecimalField(max_digits=7, decimal_places=2)
    costo_recorrido = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.vehiculo)

    class Meta:
        verbose_name = "Vehiculo de la cotizacion"
        verbose_name_plural = "Vehiculos de la cotizacion"
        ordering = ['cotizacion', 'cotizacion']


class Cotizacion_direccion(models.Model):
    """docstring for Cotizacion_direccion"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion_direccion, self).__init__(*args, **kwargs)

    cotizacion = models.ForeignKey(Cotizacion)
    direccion = models.CharField(max_length=550)
    tipo_direccion = models.CharField(max_length=100)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.direccion)

    class Meta:
        verbose_name = "direccion de la cotizacion"
        verbose_name_plural = "direcciones de la cotizacion"
        ordering = ['cotizacion', 'direccion']


class Cotizacion_trabajador(models.Model):
    """docstring for Cotizacion_trabajador"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion_trabajador, self).__init__(*args, **kwargs)

    cargo = models.ForeignKey(Cargo_trabajador)
    cotizacion = models.ForeignKey(Cotizacion)
    tarifa = models.DecimalField(max_digits=7, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    total_sin_recargo = models.DecimalField(max_digits=7, decimal_places=2)
    nocturno = models.BooleanField(default=None)
    fin_semana = models.BooleanField(default=None)
    recargo_nocturno = models.DecimalField(max_digits=7, decimal_places=2)
    recargo_fin_semana = models.DecimalField(max_digits=7, decimal_places=2)
    total_con_recargo = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.cargo)

    class Meta:
        verbose_name = "trabajador de la cotizacion"
        verbose_name_plural = "trabajadores de la cotizacion"
        ordering = ['cotizacion', 'cargo']


class Cotizacion_Ambiente(models.Model):
    """docstring for Cotizacion_Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion_Ambiente, self).__init__(*args, **kwargs)

    cotizacion = models.ForeignKey(Cotizacion)
    ambiente = models.ForeignKey(Ambiente)
    piso = models.ForeignKey(Piso)
    cantidad_muebles = models.DecimalField(max_digits=5, decimal_places=2)
    volumen_muebles = models.DecimalField(max_digits=7, decimal_places=2)
    peso_muebles = models.DecimalField(max_digits=7, decimal_places=2)
    cantidad_contenedores = models.DecimalField(max_digits=5, decimal_places=2)
    volumen_contenedores = models.DecimalField(max_digits=7, decimal_places=2)
    peso_contenedores = models.DecimalField(max_digits=7, decimal_places=2)
    volumen_contenidos = models.DecimalField(max_digits=7, decimal_places=2)
    peso_contenidos = models.DecimalField(max_digits=7, decimal_places=2)
    peso_materiales = models.DecimalField(max_digits=7, decimal_places=2)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.ambiente)

    class Meta:
        verbose_name = "Ambiente de la cotizacion"
        verbose_name_plural = "Ambientes de la cotizacion"
        ordering = ['cotizacion', 'ambiente']


class Cotizacion_Mueble(models.Model):
    """docstring for Cotizacion_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion_Mueble, self).__init__(*args, **kwargs)

    cotizacion_ambiente = models.ForeignKey(Cotizacion_Ambiente)
    mueble = models.ForeignKey(Mueble)
    tamano = models.CharField(max_length=100)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    alto = models.DecimalField(max_digits=5, decimal_places=2)
    largo = models.DecimalField(max_digits=5, decimal_places=2)
    volumen = models.DecimalField(max_digits=7, decimal_places=2)
    capacidad = models.DecimalField(max_digits=5, decimal_places=2)
    ocupacion = models.DecimalField(max_digits=5, decimal_places=2)
    forma = models.CharField(max_length=100)
    trasladable = models.BooleanField(default=None)
    apilable = models.BooleanField(default=None)
    capacidad_carga = models.BooleanField(default=None)
    capacidad_interna = models.BooleanField(default=None)
    observaciones = models.TextField(blank=True)
    densidad = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.mueble, self.cotizacion_ambiente)

    class Meta:
        verbose_name = "Mueble del Ambiente"
        verbose_name_plural = "Muebles del Ambiente"
        ordering = ['cotizacion_ambiente', 'mueble']


class Cotizacion_Contenido(models.Model):
    """docstring for Cotizacion_Contenido"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion_Contenido, self).__init__(*args, **kwargs)

    cotizacion_mueble = models.ForeignKey(Cotizacion_Mueble)
    contenido = models.ForeignKey(Contenido)
    densidad = models.DecimalField(max_digits=5, decimal_places=2)
    volumen_contenido = models.DecimalField(max_digits=5, decimal_places=2)
    peso_contenido = models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion_mueble, self.contenido)

    class Meta:
        verbose_name = "contenido en el contenedor"
        verbose_name_plural = "contenidos en el contenedor"
        ordering = ['cotizacion_mueble', 'contenido']


class Cotizacion_Servicio(models.Model):
    """docstring for Cotizacion_Servicio"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion_Servicio, self).__init__(*args, **kwargs)

    cotizacion_mueble = models.ForeignKey(Cotizacion_Mueble)
    servicio = models.ForeignKey(Servicio)
    cotizacion_contenido = models.ForeignKey(Cotizacion_Contenido, null=True, blank=True)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion_mueble, self.servicio)

    class Meta:
        verbose_name = "Servicio del mueble"
        verbose_name_plural = "Servicios del mueble"
        ordering = ['cotizacion_mueble', 'servicio']


class Cotizacion_Material(models.Model):
    """docstring for Cotizacion_Material"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion_Material, self).__init__(*args, **kwargs)

    cotizacion_servicio = models.ForeignKey(Cotizacion_Servicio)
    material = models.ForeignKey(Material)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=7, decimal_places=2)
    precio_total = models.DecimalField(max_digits=7, decimal_places=2)
    peso_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    peso_total = models.DecimalField(max_digits=5, decimal_places=2)
    recuperable = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion_mueble, self.material)

    class Meta:
        verbose_name = "Material del mueble"
        verbose_name_plural = "Materiales del mueble"
        ordering = ['cotizacion_servicio', 'material']
        unique_together = (("cotizacion_servicio", "material"),)
