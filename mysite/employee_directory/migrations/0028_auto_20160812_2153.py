# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0027_auto_20160805_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emergency_contact',
            field=models.CharField(default='NA', max_length=100, verbose_name='Emergency Contact', blank=True),
        ),
    ]
