# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-15 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nighthawk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='task_assignee',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_endpoints',
            field=models.TextField(max_length=200),
        ),
    ]
