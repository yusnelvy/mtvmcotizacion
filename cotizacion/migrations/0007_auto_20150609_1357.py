# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0006_tiempo_carga_cantidad_trabajador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='cantidad_ambientes',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cantidad_contenedores',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cantidad_muebles',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_culminacion',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_descuento',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_impuesto',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_material',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='monto_muebles',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_contenedores',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_contenidos',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_materiales',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='peso_muebles',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='total_con_impuesto',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='total_recorrido_km',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='total_sin_impuesto',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_contenedores',
            field=models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_contenidos',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_muebles_cotizado',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='volumen_muebles_sugerido',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='cantidad',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='cantidad_trabajador',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='nro_objeto_max',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='nro_objeto_min',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='peso_max',
            field=models.DecimalField(decimal_places=2, max_digits=13, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='peso_min',
            field=models.DecimalField(decimal_places=2, max_digits=13, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='volumen_max',
            field=models.DecimalField(decimal_places=2, max_digits=13, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='volumen_min',
            field=models.DecimalField(decimal_places=2, max_digits=13, blank=True, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='cantidad',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
