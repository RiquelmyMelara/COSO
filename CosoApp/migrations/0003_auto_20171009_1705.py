# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 23:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CosoApp', '0002_auto_20171009_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componente',
            old_name='coso',
            new_name='COSO',
        ),
    ]
