# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable_blog', '0002_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
