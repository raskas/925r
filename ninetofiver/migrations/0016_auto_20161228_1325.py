# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 13:25
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninetofiver', '0015_auto_20161227_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='timesheet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ninetofiver.Timesheet'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activityperformance',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4, validators=[django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(24)]),
        ),
    ]
