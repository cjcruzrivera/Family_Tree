# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20180326_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='generacion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]