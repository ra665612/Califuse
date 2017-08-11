# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0013_auto_20170717_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='bio1',
            new_name='bio',
        ),
    ]
