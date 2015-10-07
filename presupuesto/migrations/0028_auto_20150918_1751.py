# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0027_auto_20150915_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presupuesto_direccion',
            options={'ordering': ['presupuesto', 'orden'], 'verbose_name': 'direccion del presupuesto', 'verbose_name_plural': 'direcciones del presupuesto'},
        ),
        migrations.AddField(
            model_name='presupuesto_detalle',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='cargo_cliente',
            field=models.CharField(max_length=250, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='descuento_recargo',
            field=models.CharField(max_length=1, default='-'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='empresa_cliente',
            field=models.CharField(max_length=250, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='hora_estimadamudanza',
            field=models.TimeField(choices=[(datetime.time(8, 0), '8:00 am o antes'), (datetime.time(9, 0), '9:00 am'), (datetime.time(10, 0), '10:00 am'), (datetime.time(11, 0), '11:00 am'), (datetime.time(12, 0), '12:00 pm'), (datetime.time(13, 0), '01:00 pm'), (datetime.time(14, 0), '02:00 pm'), (datetime.time(15, 0), '03:00 pm'), (datetime.time(16, 0), '04:00 pm'), (datetime.time(17, 0), '05:00 pm o después')], default='08:00'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='recorrido_km',
            field=models.DecimalField(max_digits=7, choices=[(Decimal('20.00'), '20 Km o menos'), (Decimal('40.00'), 'De 21 a 40 Km'), (Decimal('60.00'), 'De 41 a 60 Km'), (Decimal('80.00'), 'De 61 a 80 Km'), (Decimal('100.00'), 'De 81 a 100 Km'), (Decimal('120.00'), 'De 101 a 120 Km'), (Decimal('140.00'), 'De 121 a 140 Km'), (Decimal('160.00'), 'De 141 a 160 Km'), (Decimal('180.00'), 'De 161 a 180 Km'), (Decimal('200.00'), '200 Km o más')], default='0.00', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.DecimalField(max_digits=7, choices=[(Decimal('1.00'), '1 hora o menos'), (Decimal('2.00'), 'De 1 a 2 horas'), (Decimal('3.00'), 'De 2 a 3 horas'), (Decimal('4.00'), 'De 3 a 4 horas'), (Decimal('5.00'), 'De 4 a 5 horas'), (Decimal('6.00'), 'De 5 a 6 horas'), (Decimal('7.00'), 'De 6 a 7 horas'), (Decimal('8.00'), 'De 7 a 8 horas'), (Decimal('9.00'), 'De 8 a 9 horas'), (Decimal('10.00'), '10 horas o más')], default='1.00', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='distancia_vehiculo',
            field=models.IntegerField(choices=[(10, '10 mts o menos'), (20, 'De 11 a 20 mts'), (30, 'De 21 a 30 mts'), (40, 'De 31 a 40 mts'), (50, 'De 41 a 50 mts'), (60, 'De 51 a 60 mts'), (70, '70 mts o más')], default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='total_m2',
            field=models.DecimalField(max_digits=7, choices=[(Decimal('40.00'), '40 m2 o menos'), (Decimal('80.00'), 'De 41 a 80 m2'), (Decimal('120.00'), 'De 81 a 120 m2'), (Decimal('160.00'), 'De 121 a 160 m2'), (Decimal('200.00'), 'De 161 a 200 m2'), (Decimal('240.00'), '240 m2 o más')], default=Decimal('0.00'), decimal_places=2),
        ),
    ]
