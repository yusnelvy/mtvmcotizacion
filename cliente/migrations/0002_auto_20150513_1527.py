# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cliente.Cliente'),
            preserve_default=True,
        ),
    ]
