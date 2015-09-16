# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0022_presupuesto_monto_descuesto_regargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='monto_materiales_revisado',
            field=models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=9),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_mundanza_revisada',
            field=models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=9),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_servicios_revisado',
            field=models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=9),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_vehiculo_revisado',
            field=models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=9),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='tipo_calculo',
            field=models.CharField(max_length=20, default='Optimizado'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='recorrido_km',
            field=models.DecimalField(max_digits=7, choices=[(Decimal('20.00'), 'Entre 1 KM a 20 KM'), (Decimal('40.00'), 'Entre 21 KM a 40 KM'), (Decimal('60.00'), 'Entre 41 KM a 60 KM'), (Decimal('80.00'), 'Entre 61 KM a 80 KM'), (Decimal('100.00'), 'Entre 81 KM a 100 KM'), (Decimal('120.00'), 'Entre 101 KM a 120 KM'), (Decimal('140.00'), 'Entre 121 KM a 140 KM'), (Decimal('160.00'), 'Entre 141 KM a 160 KM'), (Decimal('180.00'), 'Entre 161 KM a 180 KM'), (Decimal('200.00'), 'Más de 200 KM')], decimal_places=2, default='5.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.DecimalField(max_digits=7, choices=[(Decimal('1.00'), 'Entre 30 minuto a 1 hora'), (Decimal('2.00'), 'Entre 1 hora a 2 horas'), (Decimal('3.00'), 'Entre 2 horas a 3 horas'), (Decimal('4.00'), 'Entre 3 horas a 4 horas'), (Decimal('5.00'), 'Entre 4 horas a 5 horas'), (Decimal('6.00'), 'Entre 5 horas a 6 horas'), (Decimal('7.00'), 'Entre 6 horas a 7 horas'), (Decimal('8.00'), 'Entre 7 horas a 8 horas'), (Decimal('9.00'), 'Entre 8 horas a 9 horas'), (Decimal('10.00'), 'Más de 10 horas')], decimal_places=2, default='1.00'),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='distancia_vehiculo',
            field=models.IntegerField(choices=[(10, 'Menos de 10 metros'), (20, 'De 11 a 20 metros'), (30, 'De 21 a 30 metros'), (40, 'De 31 a 40 metros'), (50, 'De 41 a 50 metros'), (60, 'De 51 a 60 metros'), (70, 'Más de 70 metros')], default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='total_m2',
            field=models.DecimalField(max_digits=7, choices=[(Decimal('40.00'), 'Entre 40 metros cuadrado'), (Decimal('80.00'), 'Entre 41 a 80 metros cuadrado'), (Decimal('120.00'), 'Entre 81 a 120 metros cuadrado'), (Decimal('160.00'), 'Entre 121 a 160 metros cuadrado'), (Decimal('200.00'), 'Entre 161 a 200 metros cuadrado'), (Decimal('240.00'), 'Más de 240 metros cuadrado')], decimal_places=2, default=Decimal('0.00')),
        ),
    ]
