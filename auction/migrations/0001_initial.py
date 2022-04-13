# Generated by Django 3.2.7 on 2021-10-11 16:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('minimum_bid', models.DecimalField(decimal_places=2, max_digits=255, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='auction_images')),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('ends_on', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=255, max_length=255)),
                ('submited_on', models.DateTimeField(default=datetime.datetime.now)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.auction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
