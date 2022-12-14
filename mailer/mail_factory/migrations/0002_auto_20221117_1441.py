# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-17 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail_factory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': '\u0448\u0430\u0431\u043b\u043e\u043d',
                'verbose_name_plural': '\u0448\u0430\u0431\u043b\u043e\u043d\u044b',
            },
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='template',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mail_factory.EmailTemplate'),
        ),
    ]
