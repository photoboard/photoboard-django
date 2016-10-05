# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Group'),
        ),
        migrations.AddField(
            model_name='picture',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Subject'),
        ),
        migrations.AddField(
            model_name='picture',
            name='timetable_entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.TimetableEntry'),
        ),
        migrations.AddField(
            model_name='picture',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Topic'),
        ),
    ]