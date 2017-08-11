# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0007_auto_20170803_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default=b'ABC', unique=True, max_length=120),
        ),
    ]
