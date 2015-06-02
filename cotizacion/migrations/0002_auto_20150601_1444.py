# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cotizacion',
            options={'verbose_name_plural': 'Cotizaciones', 'ordering': ['numero_contrato'], 'verbose_name': 'Cotizacion'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_ambiente',
            options={'verbose_name_plural': 'Ambientes de la cotizacion', 'ordering': ['cotizacion', 'ambiente'], 'verbose_name': 'Ambiente de la cotizacion'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_contenedor',
            options={'verbose_name_plural': 'contenedores de la cotizacion', 'ordering': ['cotizacion_mueble', 'contenedor'], 'verbose_name': 'contenedor de la cotizacion'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_contenido',
            options={'verbose_name_plural': 'contenidos en el contenedor', 'ordering': ['cotizacion_contenedor', 'contenido'], 'verbose_name': 'contenido en el contenedor'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_direccion',
            options={'verbose_name_plural': 'direcciones de la cotizacion', 'ordering': ['cotizacion', 'direccion'], 'verbose_name': 'direccion de la cotizacion'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_material',
            options={'verbose_name_plural': 'Materiales del mueble', 'ordering': ['cotizacion_mueble', 'material'], 'verbose_name': 'Material del mueble'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_mueble',
            options={'verbose_name_plural': 'Muebles del Ambiente', 'ordering': ['cotizacion_ambiente', 'mueble'], 'verbose_name': 'Mueble del Ambiente'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_servicio',
            options={'verbose_name_plural': 'Servicios del mueble', 'ordering': ['cotizacion_mueble', 'servicio'], 'verbose_name': 'Servicio del mueble'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_trabajador',
            options={'verbose_name_plural': 'trabajadores de la cotizacion', 'ordering': ['cotizacion', 'cargo'], 'verbose_name': 'trabajador de la cotizacion'},
        ),
        migrations.AlterModelOptions(
            name='estado_cotizacion',
            options={'verbose_name_plural': 'estados', 'ordering': ['estado'], 'verbose_name': 'estado'},
        ),
        migrations.AlterModelOptions(
            name='piso',
            options={'verbose_name_plural': 'pisos', 'ordering': ['piso'], 'verbose_name': 'piso'},
        ),
        migrations.AlterModelOptions(
            name='tiempo_carga',
            options={'verbose_name_plural': 'tiempos de carga', 'ordering': ['tiempo_carga'], 'verbose_name': 'tiempo de carga'},
        ),
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name_plural': 'Vehiculos', 'ordering': ['modelo'], 'verbose_name': 'Vehiculo'},
        ),
        migrations.AlterModelOptions(
            name='vehiculo_cotizacion',
            options={'verbose_name_plural': 'Vehiculos de la cotizacion', 'ordering': ['cotizacion', 'cotizacion'], 'verbose_name': 'Vehiculo de la cotizacion'},
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='numero_contrato',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='numero_cotizacion',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='observaciones',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estado_cotizacion',
            name='estado',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='piso',
            name='piso',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
