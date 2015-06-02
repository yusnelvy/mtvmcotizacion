# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20150515_1210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes', 'ordering': ['nombre_principal'], 'verbose_name': 'Cliente'},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name_plural': 'Emails', 'ordering': ['cliente', 'email'], 'verbose_name': 'Email'},
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
    ]
