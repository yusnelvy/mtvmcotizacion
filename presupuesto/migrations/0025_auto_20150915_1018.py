# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0024_presupuesto_monto_recursos_revisado'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='cargo_cliente',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='empresa_cliente',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='fuente_promocion',
            field=models.CharField(max_length=100, default='Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='hora_creacion',
            field=models.TimeField(auto_now_add=True, default='01:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='hora_estimadamudanza',
            field=models.TimeField(default='01:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='telefono_celular',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='presupuesto_direccion',
            name='orden',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='fecha_estimadamudanza',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_materiales_revisado',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='recorrido_km',
            field=models.DecimalField(decimal_places=2, default='0.00', choices=[(Decimal('20.00'), 'Entre 1 KM a 20 KM'), (Decimal('40.00'), 'Entre 21 KM a 40 KM'), (Decimal('60.00'), 'Entre 41 KM a 60 KM'), (Decimal('80.00'), 'Entre 61 KM a 80 KM'), (Decimal('100.00'), 'Entre 81 KM a 100 KM'), (Decimal('120.00'), 'Entre 101 KM a 120 KM'), (Decimal('140.00'), 'Entre 121 KM a 140 KM'), (Decimal('160.00'), 'Entre 141 KM a 160 KM'), (Decimal('180.00'), 'Entre 161 KM a 180 KM'), (Decimal('200.00'), 'Más de 200 KM')], max_digits=7),
        ),
    ]
