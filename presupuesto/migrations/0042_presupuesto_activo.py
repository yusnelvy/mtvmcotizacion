# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondocumento', '0001_initial'),
        ('presupuesto', '0041_auto_20151019_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='activo',
            field=models.ForeignKey(default=1, to='gestiondocumento.EstadoDocumento'),
            preserve_default=False,
        ),
    ]
