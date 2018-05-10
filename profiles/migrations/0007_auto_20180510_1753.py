# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20180510_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='login_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя'),
        ),
    ]
