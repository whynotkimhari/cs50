# Generated by Django 4.2.4 on 2023-08-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_rename_last_price_bid_price_remove_bid_bidding_times_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='bid',
            name='listing_id',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AddField(
            model_name='bid',
            name='user_id',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AddField(
            model_name='comment',
            name='listing_id',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.CharField(default=0, max_length=64),
        ),
    ]