# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='c_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Employer'),
        ),
    ]
