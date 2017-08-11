# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0003_auto_20170309_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
