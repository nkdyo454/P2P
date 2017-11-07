# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_look_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mac', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='look',
            name='mac',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]