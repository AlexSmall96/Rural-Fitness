# Generated by Django 3.2.18 on 2023-05-25 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classbooking_app', '0029_auto_20230525_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.CharField(default='test_image', max_length=5000),
        ),
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 25, 13, 16, 45, 529353)),
        ),
    ]
