# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0004_contenido_tipico_predefinido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido_servicio',
            name='contenido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenido.Contenido'),
        ),
        migrations.AlterField(
            model_name='contenido_servicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Servicio'),
        ),
        migrations.AlterField(
            model_name='contenido_tipico',
            name='contenido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenido.Contenido'),
        ),
        migrations.AlterField(
            model_name='contenido_tipico',
            name='mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Mueble'),
        ),
    ]
