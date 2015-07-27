# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0002_auto_20150715_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presupuesto_servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=100)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=7)),
                ('material', models.TextField()),
                ('monto_material', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volumen_material', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso_material', models.DecimalField(decimal_places=2, max_digits=5)),
                ('detalle_presupuesto', models.ForeignKey(to='presupuesto.Presupuesto_Detalle')),
            ],
            options={
                'ordering': ['detalle_presupuesto', 'servicio'],
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
