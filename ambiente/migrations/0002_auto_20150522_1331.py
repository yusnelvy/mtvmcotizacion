# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ambiente',
            options={'verbose_name_plural': 'Ambientes', 'ordering': ['ambiente'], 'verbose_name': 'Ambiente'},
        ),
        migrations.AlterModelOptions(
            name='ambiente_tipo_inmueble',
            options={'verbose_name_plural': 'Ambientes por tipos de inmueble', 'ordering': ['tipo_inmueble', 'ambiente'], 'verbose_name': 'Ambiente por tipo inmueble'},
        ),
        migrations.AlterModelOptions(
            name='tipo_ambiente',
            options={'verbose_name_plural': 'Tipos de ambiente', 'ordering': ['tipo_ambiente'], 'verbose_name': 'Tipo de ambiente'},
        ),
    ]
