# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connor', '0009_dissertation_totalrefcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='dissertation',
            name='HIGHTREF',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dissertation',
            name='HOT',
            field=models.BooleanField(default=False),
        ),
    ]
