# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='user',
        ),
        migrations.AddField(
            model_name='phone',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='profile.Profile'),
            preserve_default=False,
        ),
    ]