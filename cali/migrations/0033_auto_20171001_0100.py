# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0032_auto_20171001_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=b'https://eliaslealblog.files.wordpress.com/2014/03/user-200.png', upload_to=b'profile_image'),
        ),
    ]
