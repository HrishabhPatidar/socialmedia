# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-23 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20180123_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.FileField(upload_to='images/%y/%m/%d'),
        ),
    ]
