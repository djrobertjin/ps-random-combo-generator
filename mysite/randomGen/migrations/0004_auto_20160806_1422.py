# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomGen', '0003_auto_20160806_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trick',
            name='position_choices',
            field=models.CharField(choices=[('fingers', 'fingers'), ('thumb', 'thumb'), ('palm', 'palm')], max_length=2),
        ),
    ]