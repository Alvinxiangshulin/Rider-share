# Generated by Django 3.0.2 on 2020-02-05 19:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200205_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 19, 10, 15, 162575, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ride',
            name='sharer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
