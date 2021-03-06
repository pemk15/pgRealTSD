# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-13 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180613_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalist',
            name='attribute',
            field=models.CharField(choices=[('r', 'Waiting processes'), ('b', 'Sleeping processes'), ('swpd', 'Virtual memory'), ('free', 'Idle memory'), ('buff', 'Memory used as buffers'), ('cache', 'Memory used as cache'), ('inact', 'Inactive memory'), ('active', 'Active memory'), ('si', 'Memory swapped in'), ('so', 'Memory swapped out'), ('bi', 'IO (in)'), ('bo', 'IO (out)'), ('in', 'System interrupts per second'), ('cs', 'Context switches per second'), ('us', 'CPU User time'), ('sy', 'CPU System time'), ('id', 'CPU Idle time'), ('wa', 'CPU IO wait time'), ('st', 'CPU Stolen from a virtual machine time')], max_length=8),
        ),
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
