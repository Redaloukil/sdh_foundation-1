# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-29 14:23
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20170829_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]