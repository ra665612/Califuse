# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0008_auto_20170803_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default=b'ABC', max_length=120),
        ),
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default=b'ABC', unique=True, max_length=120),
        ),
    ]
