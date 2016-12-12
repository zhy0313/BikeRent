# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0006_auto_20161203_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderEndTime',
            field=models.DateField(),
        ),
    ]
