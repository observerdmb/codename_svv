# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to='profiles/<function upload_to at 0x03732198>/photo', verbose_name='Фото'),
        ),
    ]
