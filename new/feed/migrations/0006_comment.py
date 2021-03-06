# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-08 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20170308_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='feed.story')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
