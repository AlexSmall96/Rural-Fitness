# Generated by Django 3.2.18 on 2023-05-12 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classbooking_app', '0021_auto_20230512_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 12, 13, 16, 46, 681608)),
        ),
    ]
