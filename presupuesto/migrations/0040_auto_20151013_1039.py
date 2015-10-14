# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0039_presupuesto_detalle_descripcion_densidadcontenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='hora_estimadamudanza',
            field=models.TimeField(default='08:00', choices=[(datetime.time(8, 0), '08:00 am o antes'), (datetime.time(9, 0), '09:00 am'), (datetime.time(10, 0), '10:00 am'), (datetime.time(11, 0), '11:00 am'), (datetime.time(12, 0), '12:00 pm'), (datetime.time(13, 0), '01:00 pm'), (datetime.time(14, 0), '02:00 pm'), (datetime.time(15, 0), '03:00 pm'), (datetime.time(16, 0), '04:00 pm'), (datetime.time(17, 0), '05:00 pm o después')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='presupuesto',
            field=models.ForeignKey(to='presupuesto.Presupuesto'),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='presupuesto',
            field=models.ForeignKey(to='presupuesto.Presupuesto'),
        ),
    ]
