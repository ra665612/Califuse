# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0020_auto_20170913_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='major',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='backimage',
            field=models.ImageField(null=True, upload_to=b'profile_image', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to=b'profile_image', blank=True),
        ),
    ]
