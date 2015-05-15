# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0002_auto_20150513_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complejidad_inmueble',
            options={'verbose_name': 'complejidad del inmueble', 'verbose_name_plural': 'complejidades del inmueble'},
        ),
        migrations.AlterModelOptions(
            name='tipo_inmueble',
            options={'verbose_name': 'Tipo de inmueble', 'verbose_name_plural': 'Tipos de inmueble'},
        ),
        migrations.AlterField(
            model_name='direccion',
            name='cliente',
            field=models.ForeignKey(to='cliente.Cliente'),
            preserve_default=True,
        ),
    ]
