# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20150513_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name_plural': 'Emails'},
        ),
        migrations.AlterField(
            model_name='email',
            name='cliente',
            field=models.ForeignKey(to='cliente.Cliente', default=1),
            preserve_default=True,
        ),
    ]
