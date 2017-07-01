# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-04 19:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_participation', '0005_auto_20170222_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('message', models.TextField(default='')),
                ('response', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_participation.Comments')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Responses',
                'verbose_name': 'Response',
            },
        ),
    ]
