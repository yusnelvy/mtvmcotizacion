# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_tipocliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(to='cliente.TipoCliente', default=1),
            preserve_default=False,
        ),
    ]
