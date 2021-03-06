# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 02:43
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_inherit', '0002_auto_20150622_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inheritpageplaceholder',
            name='from_page',
            field=cms.models.fields.PageField(help_text='Choose a page to include its plugins into this placeholder, empty will choose current page', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Page'),
        ),
    ]
