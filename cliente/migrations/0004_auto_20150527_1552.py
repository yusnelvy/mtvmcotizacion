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
            options={'verbose_name_plural': 'Clientes', 'verbose_name': 'Cliente', 'ordering': ['nombre_principal']},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name_plural': 'Emails', 'verbose_name': 'Email', 'ordering': ['cliente', 'email']},
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=75, unique=True),
            preserve_default=True,
        ),
    ]
