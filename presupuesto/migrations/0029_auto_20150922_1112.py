# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0028_auto_20150918_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='comentario',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='recorrido_km',
            field=models.DecimalField(max_digits=7, default='0.00', decimal_places=2, choices=[(Decimal('20.00'), '20 Km o menos'), (Decimal('40.00'), '21 a 40 Km'), (Decimal('60.00'), '41 a 60 Km'), (Decimal('80.00'), '61 a 80 Km'), (Decimal('100.00'), '81 a 100 Km'), (Decimal('120.00'), '101 a 120 Km'), (Decimal('140.00'), '121 a 140 Km'), (Decimal('160.00'), '141 a 160 Km'), (Decimal('180.00'), '161 a 180 Km'), (Decimal('200.00'), '200 Km o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.DecimalField(max_digits=7, default='1.00', decimal_places=2, choices=[(Decimal('1.00'), '1 hora o menos'), (Decimal('2.00'), '1 a 2 horas'), (Decimal('3.00'), '2 a 3 horas'), (Decimal('4.00'), '3 a 4 horas'), (Decimal('5.00'), '4 a 5 horas'), (Decimal('6.00'), '5 a 6 horas'), (Decimal('7.00'), '6 a 7 horas'), (Decimal('8.00'), '7 a 8 horas'), (Decimal('9.00'), '8 a 9 horas'), (Decimal('10.00'), '10 horas o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='distancia_vehiculo',
            field=models.IntegerField(default=0, choices=[(10, '10 mts o menos'), (20, '11 a 20 mts'), (30, '21 a 30 mts'), (40, '31 a 40 mts'), (50, '41 a 50 mts'), (60, '51 a 60 mts'), (70, '70 mts o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='total_m2',
            field=models.DecimalField(max_digits=7, default=Decimal('0.00'), decimal_places=2, choices=[(Decimal('40.00'), '40 m2 o menos'), (Decimal('80.00'), '41 a 80 m2'), (Decimal('120.00'), '81 a 120 m2'), (Decimal('160.00'), '121 a 160 m2'), (Decimal('200.00'), '161 a 200 m2'), (Decimal('240.00'), '240 m2 o más')]),
        ),
    ]
