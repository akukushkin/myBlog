# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0005_tagtoanswer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TagToAnswer',
        ),
    ]
