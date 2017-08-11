# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cali', '0008_auto_20170711_2328'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
