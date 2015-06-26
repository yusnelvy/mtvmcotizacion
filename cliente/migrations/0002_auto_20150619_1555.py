# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='cliente',
            field=models.ForeignKey(to='cliente.Cliente'),
            preserve_default=True,
        ),
    ]
