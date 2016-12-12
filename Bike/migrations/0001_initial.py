# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BikeID', models.CharField(max_length=20)),
                ('BikeType', models.CharField(max_length=20)),
                ('BikeStatus', models.CharField(max_length=2)),
                ('BikeUnitPrice', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OrderStartTime', models.CharField(max_length=20)),
                ('OrderEndTime', models.CharField(max_length=20)),
                ('OrderAccountPayable', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PersonID', models.CharField(max_length=20)),
                ('PersonName', models.CharField(max_length=20)),
                ('PersonPassWord', models.CharField(max_length=20)),
                ('PersonGender', models.CharField(max_length=2)),
                ('PersonPhone', models.CharField(max_length=20)),
                ('PersonStatus', models.CharField(max_length=2)),
                ('AccountPayable', models.CharField(max_length=20)),
                ('IsAdmin', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='OrderPersonID',
            field=models.ForeignKey(to='Bike.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='OrederBikeID',
            field=models.ForeignKey(to='Bike.Bike'),
            preserve_default=True,
        ),
    ]
