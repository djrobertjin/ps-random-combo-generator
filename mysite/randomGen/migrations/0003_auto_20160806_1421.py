# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomGen', '0002_auto_20160806_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trick',
            name='position_choices',
            field=models.CharField(choices=[('fingers', 'fingers'), ('thumb', 'thumb'), ('palm', 'palm')], default='fingers', max_length=2),
        ),
    ]
