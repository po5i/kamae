# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chudan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('keyname', models.CharField(max_length=50, null=True, blank=True)),
                ('examination', models.NullBooleanField()),
                ('championship', models.NullBooleanField()),
                ('seminar', models.NullBooleanField()),
                ('gasshuku', models.NullBooleanField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='travels',
            name='user',
        ),
        migrations.DeleteModel(
            name='Travels',
        ),
    ]
