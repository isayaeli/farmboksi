# Generated by Django 3.0.3 on 2020-05-23 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20200522_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 10, 47, 17, 661436)),
        ),
        migrations.AlterField(
            model_name='wishlist_item',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 10, 47, 17, 662468)),
        ),
    ]