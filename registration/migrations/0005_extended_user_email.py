# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-11 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20170306_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='extended_user',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
