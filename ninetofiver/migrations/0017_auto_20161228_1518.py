# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninetofiver', '0016_auto_20161228_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='timesheet',
        ),
        migrations.AddField(
            model_name='leavedate',
            name='timesheet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ninetofiver.Timesheet'),
            preserve_default=False,
        ),
    ]
