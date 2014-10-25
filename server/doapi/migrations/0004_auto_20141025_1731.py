# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('doapi', '0003_auto_20141025_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataentry',
            name='pub_time',
            field=models.TimeField(default=datetime.datetime(2014, 10, 25, 17, 31, 16, 799247), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listener',
            name='max_time_value',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listener',
            name='min_time_value',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
