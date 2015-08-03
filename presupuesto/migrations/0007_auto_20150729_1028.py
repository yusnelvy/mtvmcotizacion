# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0006_presupuesto_servicio_tiempo_aplicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_carga',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=5, default='0.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=5, default='0.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_total',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=5, default='0.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='monto_material',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=7, default='0.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='peso_material',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=5, default='0.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='tarifa',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=7, default='0.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='tiempo_aplicado',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=5, default='0.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='volumen_material',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=5, default='0.00'),
        ),
    ]
