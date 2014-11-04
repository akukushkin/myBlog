# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagToAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(to='ask.Question')),
                ('tag', models.ForeignKey(to='ask.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
