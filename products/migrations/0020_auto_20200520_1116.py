# Generated by Django 3.0.3 on 2020-05-20 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200410_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 11, 16, 11, 606818)),
        ),
        migrations.AlterField(
            model_name='wishlist_item',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 11, 16, 11, 607854)),
        ),
    ]