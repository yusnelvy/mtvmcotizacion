from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

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
    (10, 'Menos de 10 metros'),
    (20, 'De 11 a 20 metros'),
    (30, 'De 21 a 30 metros'),
    (40, 'De 31 a 40 metros'),
    (50, 'De 41 a 50 metros'),
    (60, 'De 51 a 60 metros'),
    (70, 'Más de 70 metros'),
    )
METROSCUADRADO_INMUEBLE = (
    (Decimal('40.00'), 'Entre 40 metros cuadrado'),
    (Decimal('80.00'), 'Entre 41 a 80 metros cuadrado'),
    (Decimal('120.00'), 'Entre 81 a 120 metros cuadrado'),
    (Decimal('160.00'), 'Entre 121 a 160 metros cuadrado'),
    (Decimal('200.00'), 'Entre 161 a 200 metros cuadrado'),
    (Decimal('240.00'), 'Más de 240 metros cuadrado'),
    )
RECORRIDO_KM = (
    (Decimal('20.00'), 'Entre 1 KM a 20 KM'),
    (Decimal('40.00'), 'Entre 21 KM a 40 KM'),
    (Decimal('60.00'), 'Entre 41 KM a 60 KM'),
    (Decimal('80.00'), 'Entre 61 KM a 80 KM'),
    (Decimal('100.00'), 'Entre 81 KM a 100 KM'),
    (Decimal('120.00'), 'Entre 101 KM a 120 KM'),
    (Decimal('140.00'), 'Entre 121 KM a 140 KM'),
    (Decimal('160.00'), 'Entre 141 KM a 160 KM'),
    (Decimal('180.00'), 'Entre 161 KM a 180 KM'),
    (Decimal('200.00'), 'Más de 200 KM')
    )
TIEMPO_RECORRIDO = (
    (Decimal('1.00'), 'Entre 30 minuto a 1 hora'),
    (Decimal('2.00'), 'Entre 1 hora a 2 horas'),
    (Decimal('3.00'), 'Entre 2 horas a 3 horas'),
    (Decimal('4.00'), 'Entre 3 horas a 4 horas'),
    (Decimal('5.00'), 'Entre 4 horas a 5 horas'),
    (Decimal('6.00'), 'Entre 5 horas a 6 horas'),
    (Decimal('7.00'), 'Entre 6 horas a 7 horas'),
    (Decimal('8.00'), 'Entre 7 horas a 8 horas'),
    (Decimal('9.00'), 'Entre 8 horas a 9 horas'),
    (Decimal('10.00'), 'Más de 10 horas')
    )


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
    total_capacidad_vehiculo = models.DecimalField(max_digits=8, decimal_places=3,
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
    recorrido_km = models.DecimalField(choices=RECORRIDO_KM, max_digits=7, decimal_places=2,
                                       blank=False, default='5.00')
    tiempo_recorrido = models.DecimalField(choices=TIEMPO_RECORRIDO, max_digits=7, decimal_places=2, blank=False, default='1.00')
    tiempo_servicios = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default='0.00')
    tiempo_carga = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default='0.00')
    tiempo_total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default='0.00')
    monto_vehiculo_hora = models.DecimalField(max_digits=9, decimal_places=2,
                                              blank=True, default=0.00)
    monto_vehiculo_recorrido = models.DecimalField(max_digits=9, decimal_places=2,
                                                   blank=True, default=0.00)
    monto_persona = models.DecimalField(max_digits=9, decimal_places=2,
                                        blank=True, default=0.00)
    monto_materiales = models.DecimalField(max_digits=9, decimal_places=2,
                                           blank=True, default=0.00)
    monto_servicios = models.DecimalField(max_digits=9, decimal_places=2,
                                          blank=True, default=0.00)
    monto_sin_impuesto = models.DecimalField(max_digits=9, decimal_places=2,
                                             blank=True, default=0.00)
    monto_impuesto = models.DecimalField(max_digits=9, decimal_places=2,
                                         blank=True, default=0.00)
    monto_con_impuesto = models.DecimalField(max_digits=9, decimal_places=2,
                                             blank=True, default=0.00)
    estado = models.CharField(max_length=20, default='Iniciado')
    activo = models.CharField(max_length=20, default='Activado')

    def __str__(self):
        return self.dni

    class Meta:
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"


class Presupuesto_direccion(models.Model):
    """docstring"""
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.PROTECT)
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
        ordering = ['presupuesto', 'direccion']


class Presupuesto_Detalle(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.PROTECT)
    ambiente = models.CharField(max_length=100)
    mueble = models.CharField(max_length=100)
    tamano = models.CharField(max_length=100)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    densidad = models.CharField(max_length=100)
    valor_densidad = models.DecimalField(max_digits=9, decimal_places=2)
    peso = models.DecimalField(max_digits=9, decimal_places=3)
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

    def __str__(self):
        return u' %s - %s - %s' % (self.presupuesto, self.ambiente, self.mueble)

    class Meta:
        verbose_name = "detalle del presupuesto"
        verbose_name_plural = "detalle del presupuesto"
        ordering = ['presupuesto', 'ambiente', 'mueble']


class Presupuesto_servicio(models.Model):
    detalle_presupuesto = models.ForeignKey(Presupuesto_Detalle, on_delete=models.PROTECT)
    servicio = models.CharField(max_length=100)
    monto_servicio = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default='0.00')
    material = models.TextField()
    cantidad_material = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default='0.00')
    precio_material = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default='0.00')
    monto_material = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default='0.00')
    volumen_material = models.DecimalField(max_digits=8, decimal_places=3, blank=True, default='0.000')
    peso_material = models.DecimalField(max_digits=9, decimal_places=3, blank=True, default='0.000')
    tiempo_aplicado = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default='0.00')

    def __str__(self):
        return u' %s - %s' % (self.detalle_presupuesto, self.servicio)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['detalle_presupuesto', 'servicio']


class DatosPrecargado(models.Model):
    complejidadinmueble = models.CharField(max_length=100)
    factorcomplejidadinmueble = models.DecimalField(max_digits=5, decimal_places=2)
    valorambcompleinmueble = models.DecimalField(max_digits=9, decimal_places=2)
    valorm3compleinmueble = models.DecimalField(max_digits=9, decimal_places=2)
    ocupacioninmueble = models.CharField(max_length=100)
    valorocupacioninmueble = models.DecimalField(max_digits=5, decimal_places=2)
    densidadcontenidomueble = models.DecimalField(max_digits=7, decimal_places=2)
    volcontenedormueble = models.DecimalField(max_digits=8, decimal_places=3)
    peso_contenedormueble = models.DecimalField(max_digits=9, decimal_places=3)
    capvolcontenedormueble = models.DecimalField(max_digits=8, decimal_places=3)
    cappesocontenedormueble = models.DecimalField(max_digits=9, decimal_places=3)
    tamanomueble = models.CharField(max_length=100)
    densidadmueble = models.CharField(max_length=100)
    anchomueble = models.DecimalField(max_digits=7, decimal_places=2)
    largomueble = models.DecimalField(max_digits=7, decimal_places=2)
    altomueble = models.DecimalField(max_digits=7, decimal_places=2)
    pesomueble = models.DecimalField(max_digits=9, decimal_places=3)
    valordensidadmueble = models.DecimalField(max_digits=5, decimal_places=2)
    volumenmueble = models.DecimalField(max_digits=8, decimal_places=3)
    tarifacomplejidadservicio = models.DecimalField(max_digits=9, decimal_places=2)
    factortiempocompservicio = models.DecimalField(max_digits=7, decimal_places=2)
    materialservicio = models.CharField(max_length=100)
    cantidadmaterial = models.DecimalField(max_digits=7, decimal_places=2)
    preciomaterial = models.DecimalField(max_digits=9, decimal_places=2)
    montomaterial = models.DecimalField(max_digits=9, decimal_places=2)
    volmaterial = models.DecimalField(max_digits=8, decimal_places=3)
    pesomaterial = models.DecimalField(max_digits=9, decimal_places=3)

    def __str__(self):
        return u' %s' % (self.pk)

    class Meta:
        verbose_name = "Dato Precargado"
        verbose_name_plural = "Datos Precargados"
