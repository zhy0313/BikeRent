# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='OrederBikeID',
            new_name='OrdererBikeID',
        ),
    ]
