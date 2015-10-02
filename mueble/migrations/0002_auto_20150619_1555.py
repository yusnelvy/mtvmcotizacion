# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ocupacion',
            options={'verbose_name_plural': 'Ocupaciones', 'ordering': ['id'], 'verbose_name': 'Ocupacion'},
        ),
        migrations.AlterUniqueTogether(
            name='mueble_ambiente',
            unique_together=set([('mueble', 'ambiente')]),
        ),
        migrations.AlterUniqueTogether(
            name='tamano_mueble',
            unique_together=set([('tamano', 'mueble')]),
        ),
    ]
