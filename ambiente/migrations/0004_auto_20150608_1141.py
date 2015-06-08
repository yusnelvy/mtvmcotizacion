# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0003_auto_20150527_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambiente',
            name='tipo_ambiente',
        ),
        migrations.DeleteModel(
            name='Tipo_ambiente',
        ),
    ]
