# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forma_mueble',
            options={'verbose_name_plural': 'Formas del Mueble', 'verbose_name': 'Forma del Mueble', 'ordering': ['forma']},
        ),
        migrations.AlterModelOptions(
            name='mueble',
            options={'verbose_name_plural': 'Muebles', 'verbose_name': 'Mueble', 'ordering': ['mueble']},
        ),
        migrations.AlterModelOptions(
            name='mueble_ambiente',
            options={'verbose_name_plural': 'Muebles  del Ambiente', 'verbose_name': 'Mueble del Ambiente', 'ordering': ['ambiente', 'mueble']},
        ),
        migrations.AlterModelOptions(
            name='ocupacion',
            options={'verbose_name_plural': 'Ocupaciones', 'verbose_name': 'Ocupacion', 'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='tamano_mueble',
            options={'verbose_name_plural': 'Tamanos del mueble', 'verbose_name': 'Tamano del mueble', 'ordering': ['mueble', 'tamano']},
        ),
        migrations.AlterModelOptions(
            name='tipo_mueble',
            options={'verbose_name_plural': 'Tipos de mueble', 'verbose_name': 'Tipo mueble', 'ordering': ['tipo_mueble']},
        ),
        migrations.AlterField(
            model_name='forma_mueble',
            name='forma',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mueble',
            name='mueble',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_mueble',
            name='tipo_mueble',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
    ]
