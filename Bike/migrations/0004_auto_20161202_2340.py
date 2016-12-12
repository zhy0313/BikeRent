# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0003_auto_20161202_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='BikeID',
        ),
        migrations.RemoveField(
            model_name='person',
            name='PersonID',
        ),
    ]
