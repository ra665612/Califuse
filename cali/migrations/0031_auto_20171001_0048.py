# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0030_auto_20171001_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='backimage',
            field=models.ImageField(default=b'{% static "img/kari-shea.jpg" %}', null=True, upload_to=b'profile_image', blank=True),
        ),
    ]
