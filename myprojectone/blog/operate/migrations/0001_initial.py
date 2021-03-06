# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-20 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogapp', '0001_initial'),
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collorderNo', models.CharField(max_length=50)),
                ('colldetail', models.TextField(verbose_name='收藏详情')),
                ('colltime', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
            options={
                'verbose_name': '收藏夹',
                'verbose_name_plural': '收藏夹',
                'db_table': 'Collection',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('ctime', models.DateTimeField(auto_now=True, verbose_name='评论时间')),
                ('cblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Blog')),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rcontent', models.CharField(max_length=300, verbose_name='回复内容')),
                ('rtime', models.DateTimeField(auto_now=True, verbose_name='回复时间')),
                ('rcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operate.Comment')),
                ('ruser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
            options={
                'verbose_name': '回复',
                'verbose_name_plural': '回复',
                'db_table': 'reply',
            },
        ),
    ]
