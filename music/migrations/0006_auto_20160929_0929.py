# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-29 09:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('music', '0005_auto_20160929_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='title',
            new_name='name',
        ),
    ]