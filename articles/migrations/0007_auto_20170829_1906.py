# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-29 19:06
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20170829_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='alt_text',
            field=models.CharField(default='no default txt', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='', upload_to=articles.models.upload_location, verbose_name='Image'),
        ),
    ]
