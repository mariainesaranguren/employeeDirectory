# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0020_remove_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
    ]