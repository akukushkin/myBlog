# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_auto_20141111_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagToAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
