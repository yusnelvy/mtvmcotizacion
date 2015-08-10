# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0004_auto_20150805_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mueble',
            name='forma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Forma_Mueble'),
        ),
        migrations.AlterField(
            model_name='mueble',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Ocupacion'),
        ),
        migrations.AlterField(
            model_name='mueble',
            name='tipo_mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Tipo_Mueble'),
        ),
        migrations.AlterField(
            model_name='mueble_ambiente',
            name='ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambiente.Ambiente'),
        ),
        migrations.AlterField(
            model_name='mueble_ambiente',
            name='mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Mueble'),
        ),
    ]
