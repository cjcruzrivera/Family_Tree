# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_auto_20180329_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='hermanos',
            field=models.ManyToManyField(null=True, related_name='_persona_hermanos_+', to='persona.Persona'),
        ),
    ]
