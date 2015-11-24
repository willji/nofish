# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151123_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='blog',
            field=models.CharField(default='www.nofish.cn', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutme',
            name='status',
            field=models.CharField(default='Doing something wonderful!', max_length=100),
            preserve_default=False,
        ),
    ]
