# Generated by Django 2.0.1 on 2018-01-14 13:45

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180114_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emotion',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='emotion',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=123),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Emotion',
        ),
    ]
