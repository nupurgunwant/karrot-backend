# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-10 10:08
from __future__ import unicode_literals

from django.db import migrations

import yunity.utils.models.field


class Migration(migrations.Migration):

    dependencies = [
        ('yunity', '0004_auto_20151005_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=yunity.utils.models.field.MaxLengthCharField(max_length=255, unique=True),
        ),
    ]
