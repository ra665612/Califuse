# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0033_auto_20171001_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='backimage',
            field=models.ImageField(default=b'none', upload_to=b'profile_image'),
        ),
    ]
