# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_postinstance_user_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postinstance',
            options={'ordering': ['user_post']},
        ),
        migrations.AddField(
            model_name='postinstance',
            name='plan',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='postinstance',
            name='targeted_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
