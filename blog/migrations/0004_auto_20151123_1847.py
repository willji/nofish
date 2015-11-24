# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151123_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-modified_time']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_time']},
        ),
        migrations.AddField(
            model_name='project',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 10, 47, 54, 329924, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='modified_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 10, 47, 57, 546870, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
