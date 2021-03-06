"""docstring"""

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import time
from gestiondocumento.models import EstadoDocumento


PISOS_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10 o más'),
    )

PISOS_RECORRER_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10 o más'),
    )

DISTANCIA_VEHICULO_INMUEBLE = (
    (20, '10 a 20 mts'),
    (30, '20 a 30 mts'),
    (40, '30 a 40 mts'),
    (50, '40 a 50 mts'),
    (60, '50 a 60 mts'),
    (70, '60 mts o más'),
    )

METROSCUADRADO_INMUEBLE = (
    (Decimal('40.00'), '40 m2 o menos'),
    (Decimal('80.00'), '40 a 80 m2'),
    (Decimal('120.00'), '80 a 120 m2'),
    (Decimal('160.00'), '120 a 160 m2'),
    (Decimal('200.00'), '160 a 200 m2'),
    (Decimal('240.00'), '200 m2 o más'),
    )

RECORRIDO_KM = (
    (Decimal('40.00'), '20 a 40 Km'),
    (Decimal('60.00'), '40 a 60 Km'),
    (Decimal('80.00'), '60 a 80 Km'),
    (Decimal('100.00'), '80 a 100 Km'),
    (Decimal('120.00'), '100 a 120 Km'),
    (Decimal('140.00'), '120 a 140 Km'),
    (Decimal('160.00'), '140 a 160 Km'),
    (Decimal('180.00'), '160 a 180 Km'),
    (Decimal('200.00'), '180 Km o más')
    )

TIEMPO_RECORRIDO = (
    (Decimal('2.00'), '01 a 02 horas'),
    (Decimal('3.00'), '02 a 03 horas'),
    (Decimal('4.00'), '03 a 04 horas'),
    (Decimal('5.00'), '04 a 05 horas'),
    (Decimal('6.00'), '05 a 06 horas'),
    (Decimal('7.00'), '06 a 07 horas'),
    (Decimal('8.00'), '07 a 08 horas'),
    (Decimal('9.00'), '08 a 09 horas'),
    (Decimal('10.00'), '09 horas o más')
    )

HORAS_CHOICES = (
    (time(8, 00), '08:00 am o antes'),
    (time(9, 00), '09:00 am'),
    (time(10, 00), '10:00 am'),
    (time(11, 00), '11:00 am'),
    (time(12, 00), '12:00 pm'),
    (time(13, 00), '01:00 pm'),
    (time(14, 00), '02:00 pm'),
    (time(15, 00), '03:00 pm'),
    (time(16, 00), '04:00 pm'),
    (time(17, 00), '05:00 pm o después')
    )


class Presupuesto(models.Model):
    """docstring"""
    dni = models.CharField(max_length=20)
    nombre_cliente = models.CharField(max_length=250)
    empresa_cliente = models.CharField(max_length=250, blank=True, default='')
    cargo_cliente = models.CharField(max_length=250, blank=True, default='')
    telefono = models.CharField(max_length=100)
    telefono_celular = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    cotizador = models.ForeignKey(User, related_name="creado_por")
    fecha_creacion = models.DateField(auto_now_add=True)
    hora_creacion = models.TimeField(auto_now_add=True)
    fecha_estimadamudanza = models.DateField()
    hora_estimadamudanza = models.TimeField(choices=HORAS_CHOICES, default='08:00')
    fuente_promocion = models.CharField(max_length=100)
    descripcion_vehiculo = models.TextField(blank=True, default=0)
    descripcion_persona = models.TextField(blank=True, default=0)
    cantidad_vehiculo = models.IntegerField(blank=True, default=0)
    cantidad_ayudante = models.IntegerField(blank=True, default=0)
    cantidad_ayudanteadicional = models.IntegerField(blank=True, default=0)
    cantidad_ambientes = models.IntegerField(blank=True, default=0)
    cantidad_muebles = models.IntegerField(blank=True, default=0)
    cantidad_contenedores = models.IntegerField(blank=True, default=0)
    total_capacidad_vehiculokg = models.DecimalField(max_digits=8, decimal_places=3,
                                                     blank=True, default=0.000)
    total_capacidad_vehiculovol = models.DecimalField(max_digits=8, decimal_places=3,
                                                      blank=True, default=0.000)
    total_peso_contenedores = models.DecimalField(max_digits=9, decimal_places=3,
                                                  blank=True, default=0.000)
    total_peso_muebles = models.DecimalField(max_digits=9, decimal_places=3,
                                             blank=True, default=0.000)
    total_peso_contenidos = models.DecimalField(max_digits=9, decimal_places=3,
                                                blank=True, default=0.000)
    total_peso_materiales = models.DecimalField(max_digits=9, decimal_places=3,
                                                blank=True, default=0.000)
    total_peso_mudanza = models.DecimalField(max_digits=9, decimal_places=3,
                                             blank=True, default=0.000)
    total_volumen_muebles = models.DecimalField(max_digits=8, decimal_places=3,
                                                blank=True, default=0.000)
    total_volumen_contenedores = models.DecimalField(max_digits=8, decimal_places=3,
                                                     blank=True, default=0.000)
    total_volumen_contenidos = models.DecimalField(max_digits=8, decimal_places=3,
                                                   blank=True, default=0.000)
    total_volumen_materiales = models.DecimalField(max_digits=8, decimal_places=3,
                                                   blank=True, default=0.000)
    total_m3 = models.DecimalField(max_digits=8, decimal_places=3,
                                   blank=True, default=0.000)
    recorrido_km = models.DecimalField(choices=RECORRIDO_KM, max_digits=7,
                                       decimal_places=2, blank=False, default='0.00')
    tiempo_recorrido = models.DecimalField(choices=TIEMPO_RECORRIDO, max_digits=7,
                                           decimal_places=2, blank=False, default='1.00')
    tiempo_servicios = models.DecimalField(max_digits=7, decimal_places=2,
                                           blank=True, default='0.00')
    tiempo_carga = models.DecimalField(max_digits=7, decimal_places=2,
                                       blank=True, default='0.00')
    duracion_teorica = models.DecimalField(max_digits=7, decimal_places=2,
                                           blank=True, default='0.00')
    duracion_optima = models.DecimalField(max_digits=7, decimal_places=2,
                                          blank=True, default='0.00')
    tiempo_total = models.DecimalField(max_digits=7, decimal_places=2,
                                       blank=True, default='0.00')
    monto_vehiculo_hora = models.DecimalField(max_digits=9, decimal_places=2,
                                              blank=True, default=0.00)
    monto_vehiculo_recorrido = models.DecimalField(max_digits=9, decimal_places=2,
                                                   blank=True, default=0.00)
    monto_personateorica = models.DecimalField(max_digits=9, decimal_places=2,
                                               blank=True, default=0.00)
    monto_personaoptima = models.DecimalField(max_digits=9, decimal_places=2,
                                              blank=True, default=0.00)
    monto_materiales = models.DecimalField(max_digits=9, decimal_places=2,
                                           blank=True, default=0.00)
    monto_servicios = models.DecimalField(max_digits=9, decimal_places=2,
                                          blank=True, default=0.00)
    monto_m3_inmueble = models.DecimalField(max_digits=9, decimal_places=2,
                                            blank=True, default=0.00)
    monto_amb_inmueble = models.DecimalField(max_digits=9, decimal_places=2,
                                             blank=True, default=0.00)
    monto_mudanza_hrsdirectas = models.DecimalField(max_digits=9, decimal_places=2,
                                                    blank=True, default=0.00)
    monto_mundanza_hrsoptimas = models.DecimalField(max_digits=9, decimal_places=2,
                                                    blank=True, default=0.00)
    monto_recursos_revisado = models.DecimalField(max_digits=9, decimal_places=2,
                                                  blank=True, default=0.00)
    monto_servicios_revisado = models.DecimalField(max_digits=9, decimal_places=2,
                                                   blank=True, default=0.00)
    monto_vehiculo_revisado = models.DecimalField(max_digits=9, decimal_places=2,
                                                  blank=True, default=0.00)
    monto_materiales_revisado = models.DecimalField(max_digits=9, decimal_places=2,
                                                    blank=True, default="0.00")
    monto_mundanza_revisada = models.DecimalField(max_digits=9, decimal_places=2,
                                                  blank=True, default=0.00)
    monto_sin_impuesto = models.DecimalField(max_digits=9, decimal_places=2,
                                             blank=True, default=0.00)
    monto_impuesto = models.DecimalField(max_digits=9, decimal_places=2,
                                         blank=True, default=0.00)
    monto_con_impuesto = models.DecimalField(max_digits=9, decimal_places=2,
                                             blank=True, default=0.00)
    monto_descuento_recargo = models.DecimalField(max_digits=9, decimal_places=2,
                                                  blank=True, default=Decimal("0.00"))
    descuento_recargo = models.CharField(max_length=1, default='-')
    activo = models.ForeignKey(EstadoDocumento)
    tipo_calculo = models.CharField(max_length=20, default='Optimizado')
    comentario = models.TextField(blank=True)
    comentario_activo = models.TextField(blank=True)
    tipo_duracion = models.CharField(max_length=20, default='Optimizado')

    def __str__(self):
        return str(self.pk)

    def get_estadoactual(self):
        return self.presupuestoestado_set.filter(predefinido=True)

    def _get_cantidadobjmudanza(self):
        """docstring"""
        return self.cantidad_muebles+self.cantidad_contenedores
    cantidadobjmudanza = property(_get_cantidadobjmudanza)

    def _get_cantidadpersonaterica(self):
        """docstring"""
        return self.cantidad_vehiculo+self.cantidad_ayudante
    cantidadpersonaterica = property(_get_cantidadpersonaterica)

    def _get_cantidadpersonaoptima(self):
        """docstring"""
        return self.cantidad_vehiculo+self.cantidad_ayudante + self.cantidad_ayudanteadicional
    cantidadpersonaoptima = property(_get_cantidadpersonaoptima)

    def _get_cantidadtotalayudante(self):
        """docstring"""
        return self.cantidad_ayudante + self.cantidad_ayudanteadicional
    cantidadtotalayudante = property(_get_cantidadtotalayudante)

    # def _get_porcentajeocupacionkg(self):
    #     """docstring"""
    #     return round((self.total_peso_mudanza / self.total_capacidad_vehiculokg)*100, 2)
    # porcentajeocupacionkg = property(_get_porcentajeocupacionkg)

    def _get_porcentajeocupacionvol(self):
        """docstring"""
        return round((self.total_m3 / self.total_capacidad_vehiculovol)*100, 2)
    porcentajeocupacionvol = property(_get_porcentajeocupacionvol)

    def _get_maxrecursoteorico(self):
        """docstring"""
        return max(self.monto_m3_inmueble, self.monto_amb_inmueble, self.monto_personateorica)
    maxrecursoteorico = property(_get_maxrecursoteorico)

    def _get_maxrecursooptimo(self):
        """docstring"""
        return max(self.monto_m3_inmueble, self.monto_amb_inmueble, self.monto_personaoptima)
    maxrecursooptimo = property(_get_maxrecursooptimo)

    def _get_vehiculomonto(self):
        """docstring"""
        return self.monto_vehiculo_hora + self.monto_vehiculo_recorrido
    vehiculomonto = property(_get_vehiculomonto)

    def _get_mudanzamontorevisadotoerico(self):
        """docstring"""
        if self.tipo_calculo == 'Basico':
            if self.descuento_recargo == '-':
                monto = self.monto_mudanza_hrsdirectas - self.monto_descuento_recargo
            else:
                monto = self.monto_mudanza_hrsdirectas + self.monto_descuento_recargo
        else:
            monto = self.monto_mudanza_hrsdirectas
        return monto
    mudanzamontorevisadotoerico = property(_get_mudanzamontorevisadotoerico)

    def _get_mudanzamontorevisadooptimo(self):
        """docstring"""
        if self.tipo_calculo == 'Optimizado':
            if self.descuento_recargo == '-':
                monto = self.monto_mundanza_hrsoptimas - self.monto_descuento_recargo
            else:
                monto = self.monto_mundanza_hrsoptimas + self.monto_descuento_recargo
        else:
            monto = self.monto_mundanza_hrsoptimas
        return monto
    mudanzamontorevisadooptimo = property(_get_mudanzamontorevisadooptimo)

    def _get_mudanzamontorevisado(self):
        """docstring"""
        if self.tipo_calculo == 'Revisado':
            if self.descuento_recargo == '-':
                monto = self.monto_mundanza_revisada - self.monto_descuento_recargo
            else:
                monto = self.monto_mundanza_revisada + self.monto_descuento_recargo
        else:
            monto = self.monto_mundanza_revisada
        return monto

    mudanzamontorevisado = property(_get_mudanzamontorevisado)

    class Meta:
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"


class Presupuesto_direccion(models.Model):
    """docstring"""
    presupuesto = models.ForeignKey(Presupuesto)
    orden = models.IntegerField()
    direccion = models.TextField()
    tipo_direccion = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(max_length=100)
    ocupacidad_inmueble = models.CharField(max_length=100)
    valor_ocupacidad = models.DecimalField(max_digits=5, decimal_places=2,
                                           blank=True, default=0.00)
    pisos = models.IntegerField(choices=PISOS_CHOICES, default=0)
    pisos_escalera = models.IntegerField(choices=PISOS_RECORRER_CHOICES, default=0)
    rampa = models.BooleanField()
    ascensor = models.BooleanField()
    ascensor_servicio = models.BooleanField()
    pisos_ascensor_servicio = models.IntegerField(choices=PISOS_RECORRER_CHOICES, default=0)
    pisos_ascensor = models.IntegerField(choices=PISOS_RECORRER_CHOICES, default=0)
    complejidad = models.CharField(max_length=100)
    factor_complejidad = models.DecimalField(max_digits=5, decimal_places=2,
                                             blank=True, default=0.00)
    valor_ambiente_complejidad = models.DecimalField(max_digits=9, decimal_places=2,
                                                     blank=True, default=0.00)
    valor_metrocubico_complejiadad = models.DecimalField(max_digits=9, decimal_places=2,
                                                         blank=True, default=0.00)
    distancia_vehiculo = models.IntegerField(choices=DISTANCIA_VEHICULO_INMUEBLE, default=0)
    total_m2 = models.DecimalField(choices=METROSCUADRADO_INMUEBLE, default=Decimal('0.00'),
                                   max_digits=7, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.presupuesto, self.direccion)

    class Meta:
        verbose_name = "direccion del presupuesto"
        verbose_name_plural = "direcciones del presupuesto"
        ordering = ['presupuesto', 'orden']


class Presupuesto_Detalle(models.Model):
    """docstring"""
    presupuesto = models.ForeignKey(Presupuesto)
    ambiente = models.CharField(max_length=100)
    mueble = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    tamano = models.CharField(max_length=100)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    ocupacidad = models.CharField(max_length=100)
    valor_ocupacidad = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_contenedor = models.IntegerField()
    volumen_contenido = models.DecimalField(max_digits=8, decimal_places=3)
    volumen_contenedor = models.DecimalField(max_digits=8, decimal_places=3)
    volumen_mueble = models.DecimalField(max_digits=8, decimal_places=3)
    capacidad_peso_contenedor = models.DecimalField(max_digits=9, decimal_places=3)
    capacidad_volumen_contenedor = models.DecimalField(max_digits=8, decimal_places=3)
    peso_contenido = models.DecimalField(max_digits=9, decimal_places=3)
    peso_contenedor = models.DecimalField(max_digits=9, decimal_places=3)
    descripcion_contenedor = models.CharField(max_length=100)
    trasladable = models.BooleanField(default=None)
    descripcion_contenido = models.CharField(max_length=100)
    densidadcontenido = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion_densidadcontenido = models.CharField(max_length=100)

    def __str__(self):
        return u' %s - %s - %s' % (self.presupuesto, self.ambiente, self.mueble)

    class Meta:
        verbose_name = "detalle del presupuesto"
        verbose_name_plural = "detalle del presupuesto"
        ordering = ['presupuesto', 'ambiente', 'mueble']


class Presupuesto_servicio(models.Model):
    """docstring"""
    detalle_presupuesto = models.ForeignKey(Presupuesto_Detalle)
    servicio = models.CharField(max_length=100)
    monto_servicio = models.DecimalField(max_digits=9, decimal_places=2,
                                         blank=True, default='0.00')
    material = models.TextField()
    cantidad_material = models.DecimalField(max_digits=7, decimal_places=2,
                                            blank=True, default='0.00')
    precio_material = models.DecimalField(max_digits=9, decimal_places=2,
                                          blank=True, default='0.00')
    monto_material = models.DecimalField(max_digits=9, decimal_places=2,
                                         blank=True, default='0.00')
    volumen_material = models.DecimalField(max_digits=8, decimal_places=3,
                                           blank=True, default='0.000')
    peso_material = models.DecimalField(max_digits=9, decimal_places=3,
                                        blank=True, default='0.000')
    tiempo_aplicado = models.DecimalField(max_digits=7, decimal_places=2,
                                          blank=True, default='0.00')
    unidad_material = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return u' %s' % (self.servicio)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['detalle_presupuesto', 'servicio']


class DatosPrecargado(models.Model):
    """docstring"""
    complejidadinmueble = models.CharField(max_length=100)
    factorcomplejidadinmueble = models.DecimalField(max_digits=5, decimal_places=2)
    valorambcompleinmueble = models.DecimalField(max_digits=9, decimal_places=2)
    valorm3compleinmueble = models.DecimalField(max_digits=9, decimal_places=2)
    ocupacioninmueble = models.CharField(max_length=100)
    valorocupacioninmueble = models.DecimalField(max_digits=5, decimal_places=2)
    densidadbajacontenidomueble = models.DecimalField(max_digits=7, decimal_places=2)
    densidadmediacontenidomueble = models.DecimalField(max_digits=7, decimal_places=2)
    densidadaltacontenidomueble = models.DecimalField(max_digits=7, decimal_places=2)
    densidadmuyaltacontenidomueble = models.DecimalField(max_digits=7, decimal_places=2)
    volcontenedormueble = models.DecimalField(max_digits=8, decimal_places=3)
    peso_contenedormueble = models.DecimalField(max_digits=9, decimal_places=3)
    capvolcontenedormueble = models.DecimalField(max_digits=8, decimal_places=3)
    cappesocontenedormueble = models.DecimalField(max_digits=9, decimal_places=3)
    tamanomueble = models.CharField(max_length=100)
    anchomueble = models.DecimalField(max_digits=7, decimal_places=2)
    largomueble = models.DecimalField(max_digits=7, decimal_places=2)
    altomueble = models.DecimalField(max_digits=7, decimal_places=2)
    volumenmueble = models.DecimalField(max_digits=8, decimal_places=3)
    tarifacomplejidadservicio = models.DecimalField(max_digits=9, decimal_places=2)
    factortiempocompservicio = models.DecimalField(max_digits=7, decimal_places=2)
    materialservicio = models.CharField(max_length=100)
    cantidadmaterial = models.DecimalField(max_digits=7, decimal_places=2)
    preciomaterial = models.DecimalField(max_digits=9, decimal_places=2)
    montomaterial = models.DecimalField(max_digits=9, decimal_places=2)
    volmaterial = models.DecimalField(max_digits=8, decimal_places=3)
    pesomaterial = models.DecimalField(max_digits=9, decimal_places=3)
    rendimiento_peso = models.DecimalField(max_digits=9, decimal_places=3)
    rendimiento_volumen = models.DecimalField(max_digits=8, decimal_places=3)
    rendimiento_unidad = models.PositiveIntegerField()
    duracion_optimamudanza = models.DecimalField(max_digits=7, decimal_places=2)
    descripcioncontenedor = models.CharField(max_length=100)
    descripcioncontenido = models.CharField(max_length=100)
    porcentaje_variacion = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return u' %s' % (self.pk)

    class Meta:
        verbose_name = "Dato Precargado"
        verbose_name_plural = "Datos Precargados"


class PresupuestoEstado(models.Model):
    """docstring"""
    presupuesto = models.ForeignKey(Presupuesto)
    estado = models.ForeignKey(EstadoDocumento)
    fecha_registro = models.DateField(auto_now_add=True, blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.presupuesto, self.estado)

    class Meta:
        verbose_name = "Estado del presupuesto"
        verbose_name_plural = "Estados del presupuesto"
