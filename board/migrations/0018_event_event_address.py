# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 23:22
from __future__ import unicode_literals

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('board', '0017_auto_20161204_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_address',
            field=address.models.AddressField(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address'),
        ),
    ]
