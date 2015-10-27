# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0044_presupuesto_tipo_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='recorrido_km',
            field=models.DecimalField(decimal_places=2, max_digits=7, default='0.00', choices=[(Decimal('40.00'), '20 a 40 Km'), (Decimal('60.00'), '40 a 60 Km'), (Decimal('80.00'), '60 a 80 Km'), (Decimal('100.00'), '80 a 100 Km'), (Decimal('120.00'), '100 a 120 Km'), (Decimal('140.00'), '120 a 140 Km'), (Decimal('160.00'), '140 a 160 Km'), (Decimal('180.00'), '160 a 180 Km'), (Decimal('200.00'), '180 Km o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.DecimalField(decimal_places=2, max_digits=7, default='1.00', choices=[(Decimal('2.00'), '01 a 02 horas'), (Decimal('3.00'), '02 a 03 horas'), (Decimal('4.00'), '03 a 04 horas'), (Decimal('5.00'), '04 a 05 horas'), (Decimal('6.00'), '05 a 06 horas'), (Decimal('7.00'), '06 a 07 horas'), (Decimal('8.00'), '07 a 08 horas'), (Decimal('9.00'), '08 a 09 horas'), (Decimal('10.00'), '09 horas o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='distancia_vehiculo',
            field=models.IntegerField(default=0, choices=[(20, '10 a 20 mts'), (30, '20 a 30 mts'), (40, '30 a 40 mts'), (50, '40 a 50 mts'), (60, '50 a 60 mts'), (70, '60 mts o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='total_m2',
            field=models.DecimalField(decimal_places=2, max_digits=7, default=Decimal('0.00'), choices=[(Decimal('40.00'), '40 m2 o menos'), (Decimal('80.00'), '40 a 80 m2'), (Decimal('120.00'), '80 a 120 m2'), (Decimal('160.00'), '120 a 160 m2'), (Decimal('200.00'), '160 a 200 m2'), (Decimal('240.00'), '200 m2 o más')]),
        ),
    ]
