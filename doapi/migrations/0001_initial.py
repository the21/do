# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('d_type', models.IntegerField(default=0, choices=[(0, b'UNKNOWN'), (1, b'TEMP'), (2, b'SOUND'), (3, b'LIGHT')])),
                ('value', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('pub_time', models.TimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(related_name=b'events', to='doapi.DataEntry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=120)),
                ('d_type', models.IntegerField(default=0, choices=[(0, b'UNKNOWN'), (1, b'TEMP'), (2, b'SOUND'), (3, b'LIGHT')])),
                ('save_all_checks', models.BooleanField(default=False)),
                ('min_value', models.IntegerField(default=0)),
                ('max_value', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('min_time_value', models.TimeField(null=True, blank=True)),
                ('max_time_value', models.TimeField(null=True, blank=True)),
                ('creator', models.ForeignKey(related_name=b'listeners', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='listener',
            field=models.ForeignKey(related_name=b'events', to='doapi.Listener'),
            preserve_default=True,
        ),
    ]
