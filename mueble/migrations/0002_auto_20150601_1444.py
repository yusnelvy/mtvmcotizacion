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
            options={'verbose_name_plural': 'Formas del Mueble', 'ordering': ['forma'], 'verbose_name': 'Forma del Mueble'},
        ),
        migrations.AlterModelOptions(
            name='mueble',
            options={'verbose_name_plural': 'Muebles', 'ordering': ['mueble'], 'verbose_name': 'Mueble'},
        ),
        migrations.AlterModelOptions(
            name='mueble_ambiente',
            options={'verbose_name_plural': 'Muebles  del Ambiente', 'ordering': ['ambiente', 'mueble'], 'verbose_name': 'Mueble del Ambiente'},
        ),
        migrations.AlterModelOptions(
            name='ocupacion',
            options={'verbose_name_plural': 'Ocupaciones', 'ordering': ['descripcion'], 'verbose_name': 'Ocupacion'},
        ),
        migrations.AlterModelOptions(
            name='tamano_mueble',
            options={'verbose_name_plural': 'Tamanos del mueble', 'ordering': ['mueble', 'tamano'], 'verbose_name': 'Tamano del mueble'},
        ),
        migrations.AlterModelOptions(
            name='tipo_mueble',
            options={'verbose_name_plural': 'Tipos de mueble', 'ordering': ['tipo_mueble'], 'verbose_name': 'Tipo mueble'},
        ),
        migrations.AlterField(
            model_name='forma_mueble',
            name='forma',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mueble',
            name='mueble',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='descripcion',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_mueble',
            name='tipo_mueble',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
