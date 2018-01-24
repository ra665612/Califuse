# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0003_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
