# Generated by Django 2.2.3 on 2019-07-23 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20190723_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 0, 11, 21, 167577)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 0, 11, 21, 167577)),
        ),
    ]
