# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170430_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_rate', models.FloatField()),
                ('additional_cost', models.FloatField()),
                ('shift_date', models.DateField()),
                ('total_hours', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Employer')),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='company',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
        migrations.DeleteModel(
            name='Shift',
        ),
    ]