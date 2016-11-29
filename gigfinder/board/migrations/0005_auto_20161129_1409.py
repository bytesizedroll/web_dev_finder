# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20161129_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_posting',
            name='job_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='musician_advertisement',
            name='ad_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
