# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0015_auto_20160801_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='NA', max_length=30, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='title',
            field=models.CharField(blank=True, max_length=40, verbose_name='Title'),
        ),
    ]
