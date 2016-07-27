# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0010_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Updated at'),
        ),
    ]