# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainproj', '0003_auto_20170728_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_pic',
        ),
    ]
