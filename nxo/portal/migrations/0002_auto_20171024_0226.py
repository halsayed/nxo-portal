# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
