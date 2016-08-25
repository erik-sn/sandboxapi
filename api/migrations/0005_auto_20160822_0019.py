# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160821_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(db_column='created', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='modified',
            field=models.DateTimeField(db_column='edited', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='markup',
            name='created',
            field=models.DateTimeField(blank=True, db_column='created', default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='modified',
            field=models.DateTimeField(blank=True, db_column='modified', default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomessage',
            name='created',
            field=models.DateTimeField(blank=True, db_column='created', default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomessage',
            name='modified',
            field=models.DateTimeField(blank=True, db_column='modified', default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(db_column='created', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tag',
            name='modified',
            field=models.DateTimeField(db_column='edited', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(blank=True, db_column='created', default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='modified',
            field=models.DateTimeField(blank=True, db_column='modified', default=django.utils.timezone.now, null=True),
        ),
    ]
