# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0002_auto_20150619_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente_tipo_inmueble',
            name='ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambiente.Ambiente'),
        ),
        migrations.AlterField(
            model_name='ambiente_tipo_inmueble',
            name='tipo_inmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Tipo_Inmueble'),
        ),
    ]
