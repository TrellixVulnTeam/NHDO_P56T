# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhdo_main', '0004_profile_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral_response',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
