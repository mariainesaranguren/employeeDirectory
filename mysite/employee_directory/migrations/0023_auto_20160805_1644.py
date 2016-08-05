# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0022_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='allergies',
            field=models.CharField(default='None', max_length=40, verbose_name='Allergies', blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='blood_type',
            field=models.CharField(default='NA', max_length=3, verbose_name='Blood Type', blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emergency_contact',
            field=models.CharField(default='NA', max_length=100, verbose_name='Emergency Contact'),
        ),
        migrations.AddField(
            model_name='employee',
            name='personal_email',
            field=models.EmailField(max_length=40, null=True, verbose_name='Personal Email', blank=True),
        ),
    ]
