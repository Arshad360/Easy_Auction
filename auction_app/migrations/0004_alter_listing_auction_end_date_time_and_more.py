# Generated by Django 4.0.3 on 2022-04-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0003_listing_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='auction_end_date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
