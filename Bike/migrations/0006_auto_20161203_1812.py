# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0005_auto_20161203_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderEndTime',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderStartTime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
