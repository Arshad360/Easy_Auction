# Generated by Django 4.0.3 on 2022-04-07 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0005_remove_listing_category_remove_listing_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='created',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='user',
        ),
    ]
