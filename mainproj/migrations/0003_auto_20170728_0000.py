# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainproj', '0002_auto_20170727_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(upload_to=b'profile_image', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=0, auto_now=True),
            preserve_default=False,
        ),
    ]
