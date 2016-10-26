# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='TITULO RECORDATORIO', max_length=80)),
                ('fecha', models.DateTimeField(blank=True, null=True, verbose_name='recordatoreo')),
                ('hora', models.TimeField()),
                ('repetir_cada', models.IntegerField(default=3)),
                ('mensaje', models.CharField(default='TITULO RECORDATORIO', max_length=80)),
            ],
        ),
    ]