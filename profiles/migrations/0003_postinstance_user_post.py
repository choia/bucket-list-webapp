# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_user'),
        ('profiles', '0002_postinstance_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='postinstance',
            name='user_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]
