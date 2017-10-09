# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Epin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epin', models.CharField(max_length=20)),
                ('tran_number', models.IntegerField()),
                ('tran_date', models.DateField(auto_now=True)),
                ('jo_type', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='kyc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.FileField(upload_to='images')),
                ('passport', models.FileField(upload_to='images')),
                ('pan', models.FileField(upload_to='images')),
                ('aadhar', models.FileField(upload_to='images')),
                ('voter', models.FileField(blank=True, null=True, upload_to='images')),
                ('cancelled_cheque', models.FileField(blank=True, null=True, upload_to='images')),
                ('passbook', models.FileField(upload_to='images')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
