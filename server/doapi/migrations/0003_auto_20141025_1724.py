# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doapi', '0002_listener_d_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listener',
            name='title',
            field=models.CharField(default=b'', max_length=120),
            preserve_default=True,
        ),
    ]
