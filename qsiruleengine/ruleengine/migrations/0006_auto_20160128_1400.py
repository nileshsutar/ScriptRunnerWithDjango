# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruleengine', '0005_remove_rulescheduler_rulename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureurls',
            name='featureurlfields',
            field=models.ManyToManyField(related_name='featureurls', to='ruleengine.FeatureFields'),
        ),
    ]