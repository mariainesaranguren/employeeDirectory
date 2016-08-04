# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_directory', '0021_remove_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='employee_directory/NoPhotoDefault.gif', upload_to='employee_directory', verbose_name='Photo', blank=True),
        ),
    ]
