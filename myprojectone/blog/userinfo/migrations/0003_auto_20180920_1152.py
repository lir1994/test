# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-20 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20180919_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showinfo',
            name='nickname',
            field=models.CharField(default='我本', max_length=20, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='showinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo'),
        ),
    ]
