# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180507_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to='profiles//%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
