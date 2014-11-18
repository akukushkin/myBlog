# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_tagtoanswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagtoanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='tagtoanswer',
            name='tag',
        ),
        migrations.DeleteModel(
            name='TagToAnswer',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='ask.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='word',
            field=models.CharField(max_length=20),
        ),
    ]
