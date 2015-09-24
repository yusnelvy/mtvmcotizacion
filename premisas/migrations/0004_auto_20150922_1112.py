# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0003_fuentepromocion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]
