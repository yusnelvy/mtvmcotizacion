# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0003_auto_20150515_1210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudades', 'ordering': ['provincia', 'ciudad'], 'verbose_name': 'Ciudad'},
        ),
        migrations.AlterModelOptions(
            name='complejidad_inmueble',
            options={'verbose_name_plural': 'complejidades del inmueble', 'ordering': ['complejidad'], 'verbose_name': 'complejidad del inmueble'},
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name_plural': 'Direcciones', 'ordering': ['tipo_direccion'], 'verbose_name': 'Direccion'},
        ),
        migrations.AlterModelOptions(
            name='inmueble',
            options={'verbose_name_plural': 'Inmuebles', 'ordering': ['inmueble'], 'verbose_name': 'Inmueble'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Paises', 'ordering': ['pais'], 'verbose_name': 'Pais'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'verbose_name_plural': 'Provincias', 'ordering': ['pais', 'provincia'], 'verbose_name': 'Provincia'},
        ),
        migrations.AlterModelOptions(
            name='tipo_direccion',
            options={'verbose_name_plural': 'Tipos de direccion', 'ordering': ['tipo_direccion'], 'verbose_name': 'Tipo de direccion'},
        ),
        migrations.AlterModelOptions(
            name='tipo_inmueble',
            options={'verbose_name_plural': 'Tipos de inmueble', 'ordering': ['tipo_inmueble'], 'verbose_name': 'Tipo de inmueble'},
        ),
        migrations.AlterModelOptions(
            name='zona',
            options={'verbose_name_plural': 'Zonas', 'ordering': ['ciudad', 'zona'], 'verbose_name': 'Zona'},
        ),
        migrations.RenameField(
            model_name='zona',
            old_name='cuidad',
            new_name='ciudad',
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='ciudad',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
