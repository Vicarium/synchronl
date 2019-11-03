# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-13 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20180827_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16, verbose_name='field type'),
        ),
    ]