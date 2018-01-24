# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0036_auto_20171014_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='backimage',
            field=models.ImageField(default=b'./static_in_pro/our_static/img/default_user.png', upload_to=b'profile_image'),
        ),
    ]
