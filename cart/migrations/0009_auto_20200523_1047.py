# Generated by Django 3.0.3 on 2020-05-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20200522_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
