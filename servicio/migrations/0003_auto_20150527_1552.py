# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20150515_1212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complejidad',
            options={'verbose_name_plural': 'Complejidades', 'verbose_name': 'Complejidad', 'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='complejidad_servicio',
            options={'verbose_name_plural': 'Complejidades del Servicio', 'verbose_name': 'Complejidad del Servicio', 'ordering': ['servicio', 'complejidad']},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'Materiales', 'verbose_name': 'Material', 'ordering': ['material']},
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name_plural': 'servicios', 'verbose_name': 'servicio', 'ordering': ['servicio']},
        ),
        migrations.AlterModelOptions(
            name='servicio_material',
            options={'verbose_name_plural': 'Materiales del Servicio', 'verbose_name': 'Material del Servicio', 'ordering': ['servicio', 'material']},
        ),
        migrations.AlterField(
            model_name='complejidad',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='material',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
    ]
