# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 20:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0014_auto_20160726_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='/Users/mariainesaranguren/Wizeline/mysite/media/default.jpeg', upload_to='{{MEDIA_URL}}/media/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.CharField(blank=True, max_length=60, verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(blank=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.CharField(blank=True, max_length=60, verbose_name='Team'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
    ]