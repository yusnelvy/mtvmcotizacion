# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0003_auto_20150518_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contenedor',
            options={'verbose_name': 'contenedor', 'verbose_name_plural': 'contenedores', 'ordering': ['contenedor']},
        ),
        migrations.AlterModelOptions(
            name='contenido',
            options={'verbose_name': 'contenido', 'verbose_name_plural': 'contenidos', 'ordering': ['contenido']},
        ),
        migrations.AlterModelOptions(
            name='contenido_tipico',
            options={'verbose_name': 'Contenido Tipico', 'verbose_name_plural': 'Contenidos Tipicos', 'ordering': ['mueble', 'contenido']},
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='contenedor',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='contenido',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='densidad_alta',
            field=models.DecimalField(max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='densidad_baja',
            field=models.DecimalField(max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='densidad_media',
            field=models.DecimalField(max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='densidad_superalta',
            field=models.DecimalField(max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
