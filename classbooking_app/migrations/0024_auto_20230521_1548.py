# Generated by Django 3.2.18 on 2023-05-21 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classbooking_app', '0023_auto_20230520_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(default='test_description', max_length=200),
        ),
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.date(2023, 5, 21)),
        ),
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 21, 15, 48, 35, 10414)),
        ),
    ]
