# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0026_auto_20160805_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.CharField(default='NA', max_length=70, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='allergies',
            field=models.CharField(default='None', max_length=100, verbose_name='Allergies', blank=True),
        ),
    ]
