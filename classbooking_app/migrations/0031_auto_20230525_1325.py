# Generated by Django 3.2.18 on 2023-05-25 13:25

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classbooking_app', '0030_auto_20230525_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 25, 13, 25, 26, 1260)),
        ),
    ]
