# Generated by Django 4.2.4 on 2023-08-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_bid_listing_remove_bid_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='last_bid_id',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
