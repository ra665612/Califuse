# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainproj', '0011_auto_20170917_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pic',
            new_name='image',
        ),
    ]
