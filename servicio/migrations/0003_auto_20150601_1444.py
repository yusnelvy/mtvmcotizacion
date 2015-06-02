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
            options={'verbose_name_plural': 'Complejidades', 'ordering': ['descripcion'], 'verbose_name': 'Complejidad'},
        ),
        migrations.AlterModelOptions(
            name='complejidad_servicio',
            options={'verbose_name_plural': 'Complejidades del Servicio', 'ordering': ['servicio', 'complejidad'], 'verbose_name': 'Complejidad del Servicio'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'Materiales', 'ordering': ['material'], 'verbose_name': 'Material'},
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name_plural': 'servicios', 'ordering': ['servicio'], 'verbose_name': 'servicio'},
        ),
        migrations.AlterModelOptions(
            name='servicio_material',
            options={'verbose_name_plural': 'Materiales del Servicio', 'ordering': ['servicio', 'material'], 'verbose_name': 'Material del Servicio'},
        ),
        migrations.AlterField(
            model_name='complejidad',
            name='descripcion',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='material',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
