# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('signbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merkletree',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 13, 3, 53, 27, 304160)),
            preserve_default=True,
        ),
    ]
