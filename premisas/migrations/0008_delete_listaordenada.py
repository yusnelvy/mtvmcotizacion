# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0007_listaordenada'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListaOrdenada',
        ),
    ]
