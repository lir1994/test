# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('headimge', models.ImageField(default='normal.png', upload_to='static/images', verbose_name='头像')),
            ],
            options={
                'verbose_name': '展示信息',
                'verbose_name_plural': '展示信息',
                'db_table': 'showinfo',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('email', models.CharField(max_length=100, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'userinfo',
            },
        ),
        migrations.AddField(
            model_name='showinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo'),
        ),
    ]