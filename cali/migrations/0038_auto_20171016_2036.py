# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0037_auto_20171016_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='backimage',
            field=models.ImageField(default=b'default_user.png', upload_to=b'profile_image'),
        ),
    ]
