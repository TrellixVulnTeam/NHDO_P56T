# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhdo_main', '0026_profile_level1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='level1',
        ),
    ]