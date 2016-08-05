# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0024_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='employee_directory/NoPhotoDefault.gif', upload_to='employee_directory', verbose_name='Photo'),
        ),
    ]
