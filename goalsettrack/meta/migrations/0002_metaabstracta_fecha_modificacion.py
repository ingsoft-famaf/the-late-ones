# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metaabstracta',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
