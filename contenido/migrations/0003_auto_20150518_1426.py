# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0001_initial'),
        ('contenido', '0002_contenido_tipico'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenido_tipico',
            name='mueble',
            field=models.ForeignKey(to='mueble.Mueble'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenido',
            name='contenedor',
            field=models.ForeignKey(default=None, to='contenido.Contenedor'),
            preserve_default=False,
        ),
    ]
