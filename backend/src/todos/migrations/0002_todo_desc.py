# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='desc',
            field=models.TextField(default='lorem ipsum dolor sir amet'),
        ),
    ]