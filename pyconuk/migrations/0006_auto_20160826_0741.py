# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyconuk', '0005_auto_20160820_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='tier',
            field=models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze'), ('partner', 'partner')], max_length=255),
        ),
    ]
