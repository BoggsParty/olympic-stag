# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-11-25 23:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0008_auto_20170304_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='award_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 25, 23, 5, 42, 433082, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
