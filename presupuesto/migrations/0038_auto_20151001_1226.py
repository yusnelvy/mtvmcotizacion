# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0037_auto_20151001_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datosprecargado',
            old_name='densidadcontenidomueble',
            new_name='densidadaltacontenidomueble',
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='densidadbajacontenidomueble',
            field=models.DecimalField(default=1, decimal_places=2, max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='densidadmediacontenidomueble',
            field=models.DecimalField(default=1, decimal_places=2, max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='densidadmuyaltacontenidomueble',
            field=models.DecimalField(default=1, decimal_places=2, max_digits=7),
            preserve_default=False,
        ),
    ]
