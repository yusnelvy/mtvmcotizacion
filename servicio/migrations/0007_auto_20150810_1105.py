# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0006_auto_20150805_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complejidad_servicio',
            name='complejidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Complejidad'),
        ),
        migrations.AlterField(
            model_name='complejidad_servicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Servicio'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Unidad'),
        ),
        migrations.AlterField(
            model_name='servicio_material',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Material'),
        ),
        migrations.AlterField(
            model_name='servicio_material',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Servicio'),
        ),
    ]
