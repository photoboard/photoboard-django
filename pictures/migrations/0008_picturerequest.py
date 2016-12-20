# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0007_auto_20161024_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureRequest',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ready', models.BooleanField(default=False)),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.Picture')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]