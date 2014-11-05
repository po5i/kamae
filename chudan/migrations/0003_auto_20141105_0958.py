# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chudan', '0002_auto_20141104_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='education_leven',
            new_name='educational_level',
        ),
    ]
