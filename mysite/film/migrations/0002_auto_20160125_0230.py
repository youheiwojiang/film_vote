# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 02:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='film',
            new_name='film_res',
        ),
    ]
