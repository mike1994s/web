# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField()),
                ('text', models.TextField()),
                ('url', models.TextField()),
                ('photo', models.TextField(default=b'')),
                ('added_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-added_at'],
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('photo', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-added_at'],
            },
        ),
        migrations.AddField(
            model_name='news',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Star'),
        ),
    ]
