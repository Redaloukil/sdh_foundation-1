# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-02 00:59
from __future__ import unicode_literals

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True),
        ),
    ]
