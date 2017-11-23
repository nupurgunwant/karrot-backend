# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 17:31
from __future__ import unicode_literals
import logging

logger = logging.getLogger(__name__)

from django.db import migrations


def copy_mail_address(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for u in User.objects.all():
        if not u.unverified_email:
            logger.warning('set unverified_email field for user %s', u.email)
            u.unverified_email = u.email
            u.save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0014_user_current_group'),
    ]

    operations = [
        migrations.RunPython(copy_mail_address, migrations.RunPython.noop)
    ]

