# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0006_auto_20160321_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default='lolol', max_length=500),
            preserve_default=False,
        ),
    ]