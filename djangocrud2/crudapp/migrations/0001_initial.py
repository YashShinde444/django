# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-11 06:28
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
                ('email', models.EmailField(max_length=20)),
                ('econtact', models.CharField(max_length=20)),
            ],
        ),
    ]