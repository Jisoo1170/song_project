# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song_order',
            name='message',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
