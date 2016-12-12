# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0007_auto_20161203_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderEndTime',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderStartTime',
            field=models.CharField(max_length=30),
        ),
    ]
