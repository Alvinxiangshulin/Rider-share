# Generated by Django 3.0.2 on 2020-01-31 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200131_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='plate_number',
            field=models.CharField(default='No info', max_length=100),
        ),
    ]
