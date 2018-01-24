# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0023_auto_20170921_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
