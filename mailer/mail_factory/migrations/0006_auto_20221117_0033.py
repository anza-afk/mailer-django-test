# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-17 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail_factory', '0005_auto_20221117_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='template',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mail_factory.Template'),
        ),
    ]
