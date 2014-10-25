# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listener',
            name='d_type',
            field=models.IntegerField(default=0, choices=[(0, b'UNKNOWN'), (1, b'TEMP'), (2, b'SOUND'), (3, b'LIGHT')]),
            preserve_default=True,
        ),
    ]
