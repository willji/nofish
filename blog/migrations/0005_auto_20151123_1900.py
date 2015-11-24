# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151123_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='github',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutme',
            name='goal',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutme',
            name='mail',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutme',
            name='motto',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutme',
            name='skill',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutme',
            name='tag',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
