# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doapi', '0004_auto_20141025_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='listener',
            field=models.ForeignKey(related_name='events', to='doapi.Listener'),
            preserve_default=True,
        ),
    ]
