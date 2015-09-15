# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0002_auto_20150826_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuentePromocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuente_promocion', models.CharField(max_length=100)),
            ],
        ),
    ]
