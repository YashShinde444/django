# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2020-07-28 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('emobile', models.CharField(max_length=20)),
            ],
        ),
    ]