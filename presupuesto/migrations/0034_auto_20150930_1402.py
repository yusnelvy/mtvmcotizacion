# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0033_auto_20150930_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosprecargado',
            name='densidadmueble',
        ),
        migrations.RemoveField(
            model_name='datosprecargado',
            name='pesomueble',
        ),
        migrations.RemoveField(
            model_name='datosprecargado',
            name='valordensidadmueble',
        ),
    ]
