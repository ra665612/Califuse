# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0014_auto_20170717_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='backimage',
            field=models.ImageField(upload_to=b'profile_image', blank=True),
        ),
    ]
