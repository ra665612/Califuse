# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0022_auto_20170917_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
