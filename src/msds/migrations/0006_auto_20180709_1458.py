# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-09 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msds', '0005_auto_20180709_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='organilabnode',
            name='color',
            field=models.CharField(default='#337ab7', max_length=10),
        ),
        migrations.AddField(
            model_name='organilabnode',
            name='shape',
            field=models.CharField(choices=[('circle', 'circle'), ('database', 'database'), ('box', 'box'), ('ellipse', 'ellipse'), ('diamond', 'diamond'), ('dot', 'dot'), ('star', 'star'), ('triangle', 'triangle'), ('triangleDown', 'triangleDown')], default='ellipse', max_length=50),
        ),
    ]
