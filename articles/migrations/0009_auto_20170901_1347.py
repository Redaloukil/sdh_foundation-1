# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 13:47
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20170829_2044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-posted', '-updated'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='sources',
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(help_text='A short description to display in search restuls', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='document',
            field=models.FileField(blank=True, help_text='Document to join in article for download', null=True, upload_to=b'', verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='article',
            name='language',
            field=models.CharField(choices=[('ARABE', '\u0627\u0644\u0639\u0631\u0628\u064a\u0629'), ('ENGLISH', 'English'), ('FRENCH', 'Fran\xe7ais')], default='ARABE', max_length=60, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False, help_text='Choose whether to publish or draft the article', verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='images',
            name='alt_text',
            field=models.CharField(help_text='Descripe your image, this field is important to search engines and for web accessibility', max_length=100, verbose_name='Image description'),
        ),
    ]
