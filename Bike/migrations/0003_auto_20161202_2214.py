# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0002_auto_20161202_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='OrdererBikeID',
            new_name='OrderBikeID',
        ),
    ]
