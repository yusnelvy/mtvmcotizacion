# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0005_perzonalizacionvisual'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perzonalizacionvisual',
            options={'verbose_name': 'Perzonalización Visual', 'verbose_name_plural': 'Perzonalizaciones Visuales'},
        ),
        migrations.AlterUniqueTogether(
            name='perzonalizacionvisual',
            unique_together=set([('usuario', 'tipo')]),
        ),
    ]
