# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-23 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20180123_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.FileField(upload_to='user/%y/%m/%d'),
        ),
    ]
