# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='link_category',
            new_name='category',
        ),
    ]
