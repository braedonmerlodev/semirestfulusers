# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-26 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restful_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ninja',
            new_name='User',
        ),
    ]
