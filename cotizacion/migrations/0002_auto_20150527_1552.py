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
            options={'verbose_name_plural': 'Cotizaciones', 'verbose_name': 'Cotizacion', 'ordering': ['numero_contrato']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_ambiente',
            options={'verbose_name_plural': 'Ambientes de la cotizacion', 'verbose_name': 'Ambiente de la cotizacion', 'ordering': ['cotizacion', 'ambiente']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_contenedor',
            options={'verbose_name_plural': 'contenedores de la cotizacion', 'verbose_name': 'contenedor de la cotizacion', 'ordering': ['cotizacion_mueble', 'contenedor']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_contenido',
            options={'verbose_name_plural': 'contenidos en el contenedor', 'verbose_name': 'contenido en el contenedor', 'ordering': ['cotizacion_contenedor', 'contenido']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_direccion',
            options={'verbose_name_plural': 'direcciones de la cotizacion', 'verbose_name': 'direccion de la cotizacion', 'ordering': ['cotizacion', 'direccion']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_material',
            options={'verbose_name_plural': 'Materiales del mueble', 'verbose_name': 'Material del mueble', 'ordering': ['cotizacion_mueble', 'material']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_mueble',
            options={'verbose_name_plural': 'Muebles del Ambiente', 'verbose_name': 'Mueble del Ambiente', 'ordering': ['cotizacion_ambiente', 'mueble']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_servicio',
            options={'verbose_name_plural': 'Servicios del mueble', 'verbose_name': 'Servicio del mueble', 'ordering': ['cotizacion_mueble', 'servicio']},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_trabajador',
            options={'verbose_name_plural': 'trabajadores de la cotizacion', 'verbose_name': 'trabajador de la cotizacion', 'ordering': ['cotizacion', 'cargo']},
        ),
        migrations.AlterModelOptions(
            name='estado_cotizacion',
            options={'verbose_name_plural': 'estados', 'verbose_name': 'estado', 'ordering': ['estado']},
        ),
        migrations.AlterModelOptions(
            name='piso',
            options={'verbose_name_plural': 'pisos', 'verbose_name': 'piso', 'ordering': ['piso']},
        ),
        migrations.AlterModelOptions(
            name='tiempo_carga',
            options={'verbose_name_plural': 'tiempos de carga', 'verbose_name': 'tiempo de carga', 'ordering': ['tiempo_carga']},
        ),
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name_plural': 'Vehiculos', 'verbose_name': 'Vehiculo', 'ordering': ['modelo']},
        ),
        migrations.AlterModelOptions(
            name='vehiculo_cotizacion',
            options={'verbose_name_plural': 'Vehiculos de la cotizacion', 'verbose_name': 'Vehiculo de la cotizacion', 'ordering': ['cotizacion', 'cotizacion']},
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='numero_contrato',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='numero_cotizacion',
            field=models.CharField(max_length=100, unique=True),
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
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='piso',
            name='piso',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
    ]
