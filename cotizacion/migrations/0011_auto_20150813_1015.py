# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0010_auto_20150810_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_descuento',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_impuesto',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_material',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_muebles',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_contenedores',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_contenidos',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_materiales',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_muebles',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='tiempo_carga',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='total_con_impuesto',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='total_recorrido_tiempo',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='total_sin_impuesto',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_contenedores',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_contenidos',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_muebles_cotizado',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_muebles_sugerido',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='cantidad_contenedores',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='cantidad_muebles',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='peso_contenedores',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='peso_contenidos',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='peso_materiales',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='peso_muebles',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='volumen_contenedores',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='volumen_contenidos',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='volumen_muebles',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion_contenido',
            name='densidad',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_contenido',
            name='peso_contenido',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_contenido',
            name='volumen_contenido',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion_direccion',
            name='total_m2',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_material',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_material',
            name='peso_total',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_material',
            name='peso_unitario',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_material',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_material',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='alto',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='ancho',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='capacidad',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='largo',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='volumen',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cotizacion_servicio',
            name='tarifa',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='recargo_fin_semana',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='recargo_nocturno',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='tarifa',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='total_con_recargo',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='total_sin_recargo',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='piso',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='peso_max',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='peso_min',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='tiempo_carga',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0.01)], default=0.0, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='volumen_max',
            field=models.DecimalField(decimal_places=8, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0.001)], default=0.0, max_digits=8, blank=True),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='volumen_min',
            field=models.DecimalField(decimal_places=3, validators=[django.core.validators.MinValueValidator(0.001)], default=0.0, max_digits=8, blank=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='capacidad_peso',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tarifa_hora',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tarifa_recorrido',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='cantidad_hora',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='costo_hora',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='costo_recorrido',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='tarifa_hora',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='tarifa_recorrido',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
