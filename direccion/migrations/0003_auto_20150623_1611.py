# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0002_auto_20150623_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='provincia',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='zona',
            name='zona',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='ciudad',
            unique_together=set([('ciudad', 'provincia')]),
        ),
        migrations.AlterUniqueTogether(
            name='provincia',
            unique_together=set([('provincia', 'pais')]),
        ),
        migrations.AlterUniqueTogether(
            name='zona',
            unique_together=set([('zona', 'ciudad')]),
        ),
    ]
