# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0016_auto_20150818_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='cantidad_ayudante',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='cantidad_ayudanteadicional',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='duracion_teorica',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=7),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_amb_inmueble',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_m3_inmueble',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_mudanza_hrsdirectas',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_mundanza_hrsoptimas',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
