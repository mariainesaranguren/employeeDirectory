# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0025_auto_20160805_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='allergies',
            field=models.CharField(default='None', max_length=70, verbose_name='Allergies', blank=True),
        ),
    ]
