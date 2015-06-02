# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0002_auto_20150522_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente',
            name='tipo_ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambiente.Tipo_ambiente'),
            preserve_default=True,
        ),
    ]
