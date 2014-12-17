# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_auto_20141211_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.ImageField(upload_to=b'users'),
        ),
    ]
