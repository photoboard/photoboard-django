# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='university',
            new_name='faculty',
        ),
        migrations.AddField(
            model_name='degree',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Faculty'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.University'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
