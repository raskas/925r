# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('ninetofiver', '0001_squashed_0003_employmentcontract_work_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRelative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=2)),
                ('relation', models.CharField(max_length=255)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.userrelative_set+', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
