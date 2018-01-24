# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0021_auto_20170916_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
