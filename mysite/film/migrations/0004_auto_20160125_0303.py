# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20160125_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='show_time',
        ),
        migrations.AddField(
            model_name='film',
            name='publish_year',
            field=models.IntegerField(default=2016),
        ),
    ]