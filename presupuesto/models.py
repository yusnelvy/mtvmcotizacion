from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Presupuesto(models.Model):
    dni = models.CharField(max_length=20)
    nombre_cliente = models.CharField(max_length=250)
    telefono = models.CharField(max_length=100)
    email = models.EmailField()
    cotizador = models.ForeignKey(User, related_name="creado_por")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_estimadamudanza = models.DateTimeField()
    descripcion_vehiculo = models.TextField(blank=True, default=0)
    descripcion_persona = models.TextField(blank=True, default=0)
    cantidad_vehiculo = models.IntegerField(blank=True, default=0)
    cantidad_persona = models.IntegerField(blank=True, default=0)
    cantidad_ambientes = models.IntegerField(blank=True, default=0)
    cantidad_muebles = models.IntegerField(blank=True, default=0)
    cantidad_contenedores = models.IntegerField(blank=True, default=0)
    total_peso_contenedores = models.DecimalField(max_digits=7, decimal_places=2,
                                                  blank=True, default=0.00)
    total_peso_muebles = models.DecimalField(max_digits=5, decimal_places=2,
                                             blank=True, default=0.00)
    total_peso_contenidos = models.DecimalField(max_digits=7, decimal_places=2,
                                                blank=True, default=0.00)
    total_volumen_muebles = models.DecimalField(max_digits=5, decimal_places=2,
                                                blank=True, default=0.00)
    total_volumen_contenedores = models.DecimalField(max_digits=7, decimal_places=2,
                                                     blank=True, default=0.00)
    total_volumen_contenidos = models.DecimalField(max_digits=7, decimal_places=2,
                                                   blank=True, default=0.00)
    total_m3 = models.DecimalField(max_digits=7, decimal_places=2,
                                   blank=True, default=0.00)
    recorrido_km = models.DecimalField(max_digits=7, decimal_places=2,
                                       blank=True, default=0.00)
    tiempo_recorrido = models.TimeField(blank=True, default='00:00')
    tiempo_carga = models.TimeField(blank=True, default='00:00')
    tiempo_total = models.TimeField(blank=True, default='00:00')
    monto_vehiculo_hora = models.DecimalField(max_digits=7, decimal_places=2,
                                              blank=True, default=0.00)
    monto_vehiculo_recorrido = models.DecimalField(max_digits=7, decimal_places=2,
                                                   blank=True, default=0.00)
    monto_persona = models.DecimalField(max_digits=7, decimal_places=2,
                                        blank=True, default=0.00)
    monto_sin_impuesto = models.DecimalField(max_digits=7, decimal_places=2,
                                             blank=True, default=0.00)
    monto_impuesto = models.DecimalField(max_digits=7, decimal_places=2,
                                         blank=True, default=0.00)
    monto_con_impuesto = models.DecimalField(max_digits=7, decimal_places=2,
                                             blank=True, default=0.00)

    def __str__(self):
        return self.dni

    class Meta:
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"


class Presupuesto_direccion(models.Model):
    """docstring"""
    presupuesto = models.ForeignKey(Presupuesto)
    direccion = models.TextField()
    tipo_direccion = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(max_length=100)
    ocupacidad_inmueble = models.CharField(max_length=100)
    valor_ocupacidad = models.DecimalField(max_digits=3, decimal_places=2)
    pisos = models.IntegerField()
    pisos_escalera = models.IntegerField(blank=True, default=0)
    rampa = models.BooleanField()
    ascensor = models.BooleanField()
    ascensor_servicio = models.BooleanField()
    pisos_ascensor_servicio = models.IntegerField(blank=True, default=0)
    pisos_ascensor = models.IntegerField(blank=True, default=0)
    complejidad = models.CharField(max_length=100)
    factor_complejidad = models.DecimalField(max_digits=4, decimal_places=2)
    valor_ambiente_complejidad = models.DecimalField(max_digits=13, decimal_places=2)
    valor_metrocubico_complejiadad = models.DecimalField(max_digits=13, decimal_places=2)
    distancia_vehiculo = models.IntegerField()
    total_m2 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.presupuesto, self.direccion)

    class Meta:
        verbose_name = "direccion del presupuesto"
        verbose_name_plural = "direcciones del presupuesto"
        ordering = ['presupuesto', 'direccion']


class Presupuesto_Detalle(models.Model):
    presupuesto = models.ForeignKey(Presupuesto)
    ambiente = models.CharField(max_length=100)
    mueble = models.CharField(max_length=100)
    tamano = models.CharField(max_length=100)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    largo = models.DecimalField(max_digits=5, decimal_places=2)
    alto = models.DecimalField(max_digits=5, decimal_places=2)
    densidad = models.CharField(max_length=100)
    valor_densidad = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    ocupacidad = models.CharField(max_length=100)
    valor_ocupacidad = models.DecimalField(max_digits=3, decimal_places=2)
    cantidad_contenedor = models.IntegerField()
    volumen_contenido = models.DecimalField(max_digits=7, decimal_places=2)
    volumen_contenedor = models.DecimalField(max_digits=7, decimal_places=2)
    volumen_mueble = models.DecimalField(max_digits=7, decimal_places=2)
    capacidad_peso_contenedor = models.DecimalField(max_digits=5, decimal_places=2)
    capacidad_volumen_contenedor = models.DecimalField(max_digits=5, decimal_places=2)
    peso_contenido = models.DecimalField(max_digits=7, decimal_places=2)
    peso_contenedor = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion_contenedor = models.CharField(max_length=100)

    def __str__(self):
        return u' %s - %s - %s' % (self.presupuesto, self.ambiente, self.mueble)

    class Meta:
        verbose_name = "detalle del presupuesto"
        verbose_name_plural = "detalle del presupuesto"
        ordering = ['presupuesto', 'ambiente', 'mueble']


class Presupuesto_servicio(models.Model):
    detalle_presupuesto = models.ForeignKey(Presupuesto_Detalle)
    servicio = models.CharField(max_length=100)
    tarifa = models.DecimalField(max_digits=7, decimal_places=2)
    material = models.TextField()
    monto_material = models.DecimalField(max_digits=7, decimal_places=2)
    volumen_material = models.DecimalField(max_digits=5, decimal_places=2)
    peso_material = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.detalle_presupuesto, self.servicio)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['detalle_presupuesto', 'servicio']
